<?php
require('config.php');

class user extends mysql{
    private $table = 'users';

    public function is_exists($username) {
        $username = parent::filter($username);

        $where = "username = '$username'";
        return parent::select($this->table, $where);
    }
    public function register($username, $password) {
        $username = parent::filter($username);
        $password = parent::filter($password);

        $key_list = Array('username', 'password');
        $value_list = Array($username, md5($password));
        return parent::insert($this->table, $key_list, $value_list);
    }
    public function login($username, $password) {
        $username = parent::filter($username);
        $password = parent::filter($password);

        $where = "username = '$username'";
        $object = parent::select($this->table, $where);
        if ($object && $object->password === md5($password)) {
            return true;
        } else {
            return false;
        }
    }
    public function show_profile($username) {
        $username = parent::filter($username);

        $where = "username = '$username'";
        $object = parent::select($this->table, $where);
        return $object->profile;
    }
    public function update_profile($username, $new_profile) {
        $username = parent::filter($username);
        $new_profile = parent::filter($new_profile);

        $where = "username = '$username'";
        return parent::update($this->table, 'profile', $new_profile, $where);
    }
    public function __tostring() {
        return __class__;
    }
}

class mysql {
    private $link = null;

    public function connect($config) {
        $this->link = mysql_connect(
            $config['hostname'],
            $config['username'], 
            $config['password']
        );
        mysql_select_db($config['database']);
        mysql_query("SET sql_mode='strict_all_tables'");

        return $this->link;
    }

    public function select($table, $where, $ret = '*') {
        $sql = "SELECT $ret FROM $table WHERE $where";
        $result = mysql_query($sql, $this->link);
        return mysql_fetch_object($result);
    }

    public function insert($table, $key_list, $value_list) {
        $key = implode(',', $key_list);
        $value = '\'' . implode('\',\'', $value_list) . '\''; 
        $sql = "INSERT INTO $table ($key) VALUES ($value)";
        return mysql_query($sql);
    }

    public function update($table, $key, $value, $where) {
        $sql = "UPDATE $table SET $key = '$value' WHERE $where";
        return mysql_query($sql);
    }

    public function filter($string) {
        $escape = array('\'', '\\\\');
        $escape = '/' . implode('|', $escape) . '/';
        $string = preg_replace($escape, '_', $string);

        $safe = array('select', 'insert', 'update', 'delete', 'where');
        $safe = '/' . implode('|', $safe) . '/i';
        return preg_replace($safe, 'hacker', $string);
    }
    public function __tostring() {
        return __class__;
    }
}
session_start();
$user = new user();
$user->connect($config);
