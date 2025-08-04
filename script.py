#!/usr/bin/env python3
import sys
import platform
import subprocess
import shutil
import socket
import argparse
from pathlib import Path
import tempfile

# --- CONFIGURAÇÃO ---
REQUIRED_PY_PKGS = ["docker", "requests"]  # só checa, não instala
SUPPORTED_OS = {"Linux", "Windows"}

# caminhos relativos esperados
DNS_CONF_DIR = Path("./DNS/conf-dns")
DB_FILE_GLOB = "db.*.asa.isp"
NAMED_LOCAL = "named.conf.local"

# padrões a substituir
PATTERN_DB = "127.0.0.1"
PATTERN_NAMED = "1.1.1.1"


# --- funções de utilidade ---
def detect_os():
    return platform.system()

def ensure_supported_os(os_name):
    if os_name not in SUPPORTED_OS:
        print(f"[ERRO] Sistema operacional '{os_name}' não suportado. Só há suporte para: {', '.join(sorted(SUPPORTED_OS))}.", file=sys.stderr)
        sys.exit(2)

def check_python_packages():
    missing = []
    for pkg in REQUIRED_PY_PKGS:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    return missing

def is_docker_daemon_available():
    try:
        subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except Exception:
        return False

def find_docker_compose():
    try:
        subprocess.run(["docker", "compose", "version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return ["docker", "compose"]
    except Exception:
        pass
    if shutil.which("docker-compose"):
        try:
            subprocess.run(["docker-compose", "version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            return ["docker-compose"]
        except Exception:
            pass
    return None

def get_host_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("1.1.1.1", 80))
            return s.getsockname()[0]
    except Exception:
        pass
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if ip and not ip.startswith("127."):
            return ip
    except Exception:
        pass
    return None

def atomic_replace(file_path: Path, new_content: str):
    """
    Escreve new_content em file_path de forma atômica, criando backup .bak se ainda não existir.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} não existe.")
    bak = file_path.with_suffix(file_path.suffix + ".bak")
    if not bak.exists():
        shutil.copy2(file_path, bak)  # backup inicial
    # escreve em temporário no mesmo diretório e move
    with tempfile.NamedTemporaryFile("w", delete=False, dir=str(file_path.parent)) as tf:
        tf.write(new_content)
        tempname = tf.name
    # substituir
    Path(tempname).replace(file_path)

def replace_in_file(file_path: Path, old: str, new: str):
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"[ERRO] Falha ao ler {file_path} (problema de codificação).", file=sys.stderr)
        return False
    if old not in content:
        print(f"[AVISO] padrão '{old}' não encontrado em {file_path}; pulando.", file=sys.stderr)
        return False
    updated = content.replace(old, new)
    if updated == content:
        print(f"[INFO] Nenhuma alteração necessária em {file_path}.", file=sys.stderr)
        return False
    try:
        atomic_replace(file_path, updated)
        print(f"[OK] Substituído '{old}' por '{new}' em {file_path}. backup em {file_path.with_suffix(file_path.suffix + '.bak')}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao escrever em {file_path}: {e}", file=sys.stderr)
        return False

def process_dns_configs(host_ip: str):
    if not DNS_CONF_DIR.is_dir():
        print(f"[ERRO] Diretório esperado {DNS_CONF_DIR} não existe.", file=sys.stderr)
        return False
    success = True

    # arquivos db.*.asa.isp
    for dbf in sorted(DNS_CONF_DIR.glob(DB_FILE_GLOB)):
        replaced = replace_in_file(dbf, PATTERN_DB, host_ip)
        success = success and replaced

    # named.conf.local
    named_local_path = DNS_CONF_DIR / NAMED_LOCAL
    if named_local_path.exists():
        replaced = replace_in_file(named_local_path, PATTERN_NAMED, host_ip)
        success = success and replaced
    else:
        print(f"[AVISO] {NAMED_LOCAL} não encontrado em {DNS_CONF_DIR}.", file=sys.stderr)
        success = False

    return success

# --- entrada principal ---
def parse_args():
    parser = argparse.ArgumentParser(description="Valida ambiente Docker/IP e aplica substituições em conf-dns.")
    parser.add_argument("--export", choices=["bash", "powershell"], help="Imprime comandos de export para o shell.")
    return parser.parse_args()

def main():
    args = parse_args()

    os_name = detect_os()
    OS_TYPE = os_name  # variável inicial
    ensure_supported_os(OS_TYPE)

    status = {
        "os": OS_TYPE,
        "python_pkgs": None,
        "docker_daemon": False,
        "docker_compose_cmd": None,
        "host_ip": None,
        "file_updates": False,
    }
    exit_code = 0

    # checa pacotes python
    missing = check_python_packages()
    if missing:
        print(f"[ERRO] Pacotes Python faltando: {', '.join(missing)}", file=sys.stderr)
        status["python_pkgs"] = f"faltando: {', '.join(missing)}"
        exit_code = 1
    else:
        status["python_pkgs"] = "ok"

    # docker daemon
    if is_docker_daemon_available():
        status["docker_daemon"] = True
    else:
        print("[ERRO] Não foi possível comunicar com o daemon Docker.", file=sys.stderr)
        exit_code = 1

    # docker compose
    compose = find_docker_compose()
    if compose:
        status["docker_compose_cmd"] = " ".join(compose)
    else:
        print("[ERRO] Nem 'docker compose' nem 'docker-compose' disponíveis.", file=sys.stderr)
        exit_code = 1

    # ip
    ip = get_host_ip()
    if ip:
        status["host_ip"] = ip
    else:
        print("[AVISO] Não foi possível determinar o IP da máquina.", file=sys.stderr)

    # aplica substituições nos arquivos se tiver IP
    if status["host_ip"]:
        updated = process_dns_configs(status["host_ip"])
        status["file_updates"] = updated
        if not updated:
            print("[AVISO] Houve falhas ao atualizar arquivos de DNS.", file=sys.stderr)
            # não necessariamente fatal
    else:
        print("[ERRO] Sem IP válido, pulando alterações nos arquivos.", file=sys.stderr)
        exit_code = 1

    # resumo
    print("=== resumo ===")
    print(f"OS: {status['os']}")
    print(f"Pacotes Python: {status['python_pkgs']}")
    print(f"Docker daemon: {'acessível' if status['docker_daemon'] else 'não acessível'}")
    print(f"Compose cmd: {status['docker_compose_cmd'] or '<nenhum>'}")
    print(f"Host IP: {status['host_ip'] or '<desconhecido>'}")
    print(f"Atualização de arquivos: {'sucesso' if status['file_updates'] else 'parcial/erro'}")

    # exporta variáveis
    if args.export:
        if args.export == "bash":
            if status["docker_compose_cmd"]:
                print(f'export DOCKER_COMPOSE_CMD="{status["docker_compose_cmd"]}"')
            if status["host_ip"]:
                print(f'export HOST_IP="{status["host_ip"]}"')
            print(f'export OS_TYPE="{OS_TYPE}"')
        elif args.export == "powershell":
            if status["docker_compose_cmd"]:
                print(f'$Env:DOCKER_COMPOSE_CMD = "{status["docker_compose_cmd"]}"')
            if status["host_ip"]:
                print(f'$Env:HOST_IP = "{status["host_ip"]}"')
            print(f'$Env:OS_TYPE = "{OS_TYPE}"')

    if exit_code != 0:
        sys.exit(exit_code)
    
    def run_compose(compose_cmd):
        full = compose_cmd + ["up", "-d", "--build"]
        try:
            print(f"[INFO] Executando: {' '.join(full)}")
            subprocess.run(full, check=True)
            print("[OK] Containers levantados com sucesso.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[ERRO] 'docker compose up' falhou com código {e.returncode}.", file=sys.stderr)
            return False

    # ... dentro de main(), depois de imprimir o resumo e antes do export/exit:
    # tenta subir os containers se os pré-requisitos básicos estiverem OK
    if status["docker_daemon"] and status["docker_compose_cmd"] and status["host_ip"]:
        compose_cmd_list = status["docker_compose_cmd"].split()
        success_compose = run_compose(compose_cmd_list)
        if not success_compose:
            # erro ao subir, força saída com erro
            sys.exit(3)
    else:
        print("[AVISO] Pulando 'docker compose up' porque algum pré-requisito falhou.", file=sys.stderr)
        if not status["docker_daemon"] or not status["docker_compose_cmd"]:
            sys.exit(1)

if __name__ == "__main__":
    main()
