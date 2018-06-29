# Google CTF 2018 : DM-COLLISION

**category** : crypto

**points** : 176

**solves** : 63

## write-up

這題要找 DES collision 和 fixed point

他的 collision 是要滿足這樣 `b1.key + b1.input != b2.key + b2.input and b1.output == b2.output`

我們知道 DES 的 key 有 64 bits 但是有 8 個 bits 沒有用是拿來作 parity check 的

所以我們只要讓兩個 key 的 parity check 的 bit 不一樣其他都一樣這樣結果就不會變

再來是要滿足 `b3.output != [0] * BLOCK_SIZE` 也就是 0 pre-image

這題其實不是 DES 是 Davies–Meyer single-block-length compression function

看起來很複雜其實就只是 `Xor(DESEncrypt(inp, key), inp)`

所以要讓 ouput 是 0 代表 `inp == DESEncrypt(inp, key)`

也就是要找 DES 的 fixed point

那麼 key 是我們決定的

我們可以用 DES 的 weak key

並且我們可以在 weak key 的加密底下很輕鬆的找到 fixed point ( 請見 : [DES](https://oalieno.github.io/crypto/symmetric/des/) )

# other write-ups and resources

