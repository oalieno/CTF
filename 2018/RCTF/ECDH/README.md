# RCTF 2018 : ECDH

**category** : crypto

**points** : 416

**solves** : 29

## write-up

這題是用 elliptic curve diffie hellman 交換密鑰，然後用 AES ECB 作加密傳 flag

那我們只要能知道 key 就大功告成了

可以發現我們可以直接告訴 Alice 或 Bob 對方的 public key 是什麼

我們知道 elliptic curve diffie hellman 的 public key 是一個在橢圓曲線上點 aG，對方收到後會 b(aG)

那我們就給 Bob 一個單位元素 O ('00' * 17)

這樣他乘以什麼都是自己

所以我們就知道 AES ECB 的 key 是 b'\x00' * 16

然後就直接解密

# other write-ups and resources

