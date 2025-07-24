<?php

$config = [];

$config['db_dsnw'] = 'mysql://roundcube:roundcube@maildb/roundcube';

$config['default_host'] = 'imap://email';
$config['default_port'] = 143;

$config['smtp_server'] = 'smtp://email';
$config['smtp_port'] = 25;
$config['smtp_user'] = '%u';
$config['smtp_pass'] = '%p';

$config['language'] = 'pt_BR';
$config['locale_string'] = 'pt_BR.UTF-8';

$config['plugins'] = ['archive', 'zipdownload', 'managesieve'];

$config['skin'] = 'elastic';
$config['session_lifetime'] = 30;

$config['enable_installer'] = false;

$config['log_logins'] = true;
$config['debug_level'] = 4;
$config['log_driver'] = 'file';
$config['log_dir'] = '/var/www/html/logs';