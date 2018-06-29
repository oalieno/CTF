# Google CTF 2018 : PERFECT-SECRECY

**category** : crypto

**points** : 158

**solves** : 74

## write-up

經典的 RSA LSB Oracle Attack

server 會幫你解密並根據解密完的明文的最後一個 bit 來選擇 `p = m0 or m1`

並印出 100 個 `(p + k) % 2` 其中 `k = random.randint(0, 2)`

`m0, m1` 我們可以控制

因為 random 的範圍是 `0 ~ 2` 所以偶數會比奇數多

`(p + k) % 2` 當 p 是偶數時，結果中的偶數比奇數多  
`(p + k) % 2` 當 p 是奇數時，結果中的奇數比偶數多

這樣我們就有一個 oracle 可以知道解密出來的明文的最後一個 bit

就可以用經典的 RSA LSB Oracle Attack

詳細的理論請見 : [RSA LSB Oracle Attack](https://oalieno.github.io/crypto/asymmetric/rsa/lsb-oracle/)

flag : `CTF{h3ll0__17_5_m3_1_w45_w0nd3r1n6_1f_4f73r_4ll_7h353_y34r5_y0u_d_l1k3_70_m337}`

# other write-ups and resources

* https://github.com/showeremoji/google-ctf18-quals/tree/master/perfectsec
* https://github.com/p4-team/ctf/tree/master/2018-06-23-google-ctf/crypto_secrecy
