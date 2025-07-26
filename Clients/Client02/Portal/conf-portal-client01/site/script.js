function conectar() {
  const usuario = document.getElementById('usuario').value;
  const senha = document.getElementById('senha').value;

  if (usuario && senha) {
    alert('Conectando ao Proxy...\nUsuário: ' + usuario);
    // redirecionar ou conectar ao backend
    // window.location.href = '/proxy?user=' + encodeURIComponent(usuario);
  } else {
    alert('Por favor, preencha todos os campos.');
  }
}
