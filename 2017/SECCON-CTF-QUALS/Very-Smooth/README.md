# SECCON CTF QUALS 2017 : Very smooth

**category** : crypto

**points** : 300

> Very smooth
>
> Decrypt index.html from PCAP.
>
> Please, submit the flag in the format: "SECCON{" + Answer + "}"
>
> Answer is written in index.html
>
> https://files-quals.seccon.jp/very_smooth_36c055008b945516b9c17e2ecce1c582c184b57c2945bbffba20372a8f9a3449.zip

## write-up

[some ctf writeups](https://ctf.rip/bsides-sf-ctf-2017-root-crypto-challenge/)

[extract certificate from pcap](https://security.stackexchange.com/questions/123851/how-can-i-extract-the-certificate-from-this-pcap-file)

參考上面兩篇把 憑證 取出來存成 `certificate.der`

`openssl x509 -inform der -pubkey -noout -in certificate.cer > pub.pem` 再轉成 pem 格式的 public key

再來就是來分解 N 了 ( N 是 1024 bit )

首先用 `./RsaCtfTool.py --publickey public.pem --verbose --private` 但解不開 ( factordb 可以分解 O_O 不過應該是賽後有人把他傳上去了因為我是賽後
才解這題的 )

但是題目有提示 smooth 也就是 smooth number 也就是質因數很多的 number

那我就用 Pollard p-1 就直接解出來了 O_O ( 看 writeups 好像大家都用 Williams p+1 還沒看懂他 Orz )

解出來之後輸出成 pem 格式的 private key

![](https://i.imgur.com/x3tDP65.png)

Edit>Preference Protocol>SSL>Edit RSA keys list 把 private.pem 匯入

然後 follow SSL stream 就大功告成

![](https://i.imgur.com/yLT7EL0.png)

flag : SECCON{One of these primes is very smooth.}

## other write-ups and resources

* https://github.com/p4-team/ctf/tree/master/2017-12-09-seccon-quals/crypto_smooth
* https://ctftime.org/writeup/8309
