<?php
define('DB_TYPE', 'unix_socket');
define('DB_HOST', '/tmp/mysql.sock');
define('DB_NAME', 'sqlinj');
define('DB_USER', 'sqlinj');
define('DB_PASS', 'sqlinj');

$connection_string = sprintf('mysql:%s=%s;dbname=%s;charset=utf8mb4', DB_TYPE, DB_HOST, DB_NAME);
$db = new PDO($connection_string, DB_USER, DB_PASS);
$r = $db->query(sprintf('SELECT id, val FROM sqlinj WHERE id = %s', $_GET['id']));

$success = ($r && $r->fetchObject()) ? true : false;

echo $success ? 'True' : 'False';

$_CODE = $success ? 200 : 500;
file_put_contents("access.log", "{$_CODE} - {$_SERVER['REQUEST_METHOD']} {$_SERVER['REQUEST_URI']} HTTP/1.1\n", FILE_APPEND);

?>