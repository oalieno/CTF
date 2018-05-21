# DEFCON QUALS 2018 : official

**category** : crypto, pwn

**points** : 194

## write-up

這題是一個 DSA

有一個 one null byte overflow 可以蓋到 random nonce 的最後一個 byte

也就是我們可以知道 random nonce 的最後一個 byte 是 0x00

照著這篇 [stack overflow](https://crypto.stackexchange.com/questions/44644/how-does-the-biased-k-attack-on-ecdsa-work) 就可以解出來了

sentinel value sT, sU 都給他 1

# other write-ups and resources

