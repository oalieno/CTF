# VolgaCTF QUALS 2018 : Nonsense

**category** : crypto

**points** : 200

**solves** : 90

## write-up

這題是 Digital Signature Algorithm ( DSA )

我們知道所有的參數除了密鑰 $x$ 和 linear congruential generator ( LCG ) 的 seed

看[這篇論文](https://cseweb.ucsd.edu/~mihir/papers/dss-lcg.pdf)

以及參考一下前年的題目的 writeups [VolgaCTF QUALS 2016 : Lazy](https://github.com/yanapermana/ctf-2016/blob/master/volga-ctf-quals/crypto/lazy/Volga_CTF_Quals_2016_Lazy.pdf)

我們知道這樣

![](https://i.imgur.com/EC51KV4.png)

我們要解的是這個聯立方程式 ( k1, k2, x 未知 )

![](https://i.imgur.com/H3Oc1Mw.png)

上面那篇有解釋要如何解這樣的方程式 ( 不同模數下的聯立方程式 )

但是仔細一看發現 q 和 m 是一樣的

轉成矩陣的樣子就是這樣

![](https://i.imgur.com/rh1hZM7.png)

所有數字都是在模 q = m 下

使用 sage 來算輕鬆簡單的拿到 flag

# other write-ups and resources

* http://blog.redrocket.club/2018/03/26/VolgaCTF-Nonsense/

