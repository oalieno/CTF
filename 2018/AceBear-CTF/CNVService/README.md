# AceBear CTF 2018 : CNVService

**category** : crypto
**points** : 856

> Service: nc cnvservice.acebear.site 1337

## write-up

題目實做了一個新的 block cipher mode 叫做 CNV

有註冊和登入的功能

註冊要提供 **name** 和 **username** 伺服器會回傳 **cookie** 回來

登入要提供 **cookie**

CNV 跟 CBC 基本上長的差不多像，就差一個 md5

![](https://i.imgur.com/gIpwcRE.png)

所以我們不能像平常一樣隨意的 flip bit 了

看了一下原始碼，我們的目的很明顯就是用 root 登入，就是要把第二個 block 的開頭改成 `root*`

AES 一個 block decrypt 完的值我們叫他 `I`

我們要讓 `I = md5(cipher) ^ "root*..."` (solve.py:28)

那我們就先用一個不一樣的 name 註冊然後算出我們的 username 要放什麼讓 `username ^ md5(cipher) = I` (solve.py:30-33)

然後我們就得到 magic 加密後會得到 `I` (solve.py:35-38)

最後我們換回原本的 name 把第二個 block 用 magic 代替就大功告成了

## other write-ups and resources

* https://masterpessimistaa.wordpress.com/2018/01/31/cnvservice-acebear-ctf-2018-writeup/
