# VXCTF 2018 : Groundbreaking Conjecture

**category** : crypto, misc

**points** : 500

**solves** : 1

## write-up

這題一開始給的連結是一個 google slides

裡面有一張圖被黑色框框遮住了

那我們就建立一個副本然後把那個框框拿掉

然後還順便發現他的圖片被裁切過了把他還原就變下面這樣

![](https://i.imgur.com/aDF66Gt.png)

看起來就是 RSA

有 c, n, e 還有部份的 p

顯然這就是 known high bits of p

[sage document](http://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_modn_dense_ntl.html) 這邊有提到 partial knowledge about q

那我們先用線上辨識字元的工具把資訊拉出來 ( http://www.newocr.com/ )

然後再照著 sage document 用 coppersmith method 來解決這題

# other write-ups and resources

