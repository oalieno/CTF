# VolgaCTF QUALS 2018 : Forbidden

**category** : crypto

**points** : 300

**solves** : 47

## write-up

這題是 AES GCM

題目有給兩組 (plain, cipher, tag)

要求另一組 (plain, cipher) 的 tag

![](https://i.imgur.com/0MOQZ87.png)

整理一下就會是上面的聯立方程式

將前兩個方程式做相加會發現只剩一元多次方程式 ( 只剩 H 未知 )

那我們就求該式的根就找到 H 了

然後就求 Y

再帶入第三式就有 T3 了

AES GCM 實作的時候要注意的地方我整理在[這邊](https://oalieno.github.io/crypto/symmetric/mode/)

# other write-ups and resources

* http://blog.redrocket.club/2018/03/27/VolgaCTF-Forbidden/
