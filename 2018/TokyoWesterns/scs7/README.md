# TokyoWesterns 2018 : scs7

**category** : crypto

**points** : 112

**solves** : 134

## write-up ( English version )

```
encrypted flag: vJuBfoxCXwYd5khhq4DjGho5FzPH2WqxxQakBU5V1c8g8bFWT0Jj0u6g1nVq80Zh
You can encrypt up to 100 messages.
message:
```

After connect to server, you will get encrypted flag

Then, we can encrypt up to 100 messages

Two Observations

1.
All possible characters are `0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz`

There are total 59 characters, no `IOl`

Looks like base58, but with 59 characters ( Maybe base59 )

2.

```
message: AAAAAAAAAAAA
ciphertext: nz3BbchXx5t4HDqz
```

Second and last one are `z`

```
message: AAAAAAAAAAAA
ciphertext: 59U0mekHLR71nWb9
```

Second and last one are `9`

Looks like remapping the characters

Based on above observations

First,  we collect lots of cipher text and compare it with original base59 cipher text to figure out the mapping between characters

Then, we can just do base59 decode to get the flag

`TWCTF{67ced5346146c105075443add26fd7efd72763dd}`

## write-up ( 中文版 )

```
encrypted flag: vJuBfoxCXwYd5khhq4DjGho5FzPH2WqxxQakBU5V1c8g8bFWT0Jj0u6g1nVq80Zh
You can encrypt up to 100 messages.
message:
```

連上 server 後會拿到加密後的 flag

然後他會幫我們加密 100 個 messages

兩個觀察

1. 加密後的所有字元可能有 `0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz`，少了 `IOl`，總共 59 個，看起來就是很像 base58 的 base59

2.

```
message: AAAAAAAAAAAA
ciphertext: nz3BbchXx5t4HDqz
```

第二個和最後一個都是 `z`

```
message: AAAAAAAAAAAA
ciphertext: 59U0mekHLR71nWb9
```

第二個和最後一個都是 `9`

看起來就是把字元攪亂

所以我們就先收集收集很多密文去跟我們自己用 base59 加密出來的密文作比較，把哪個字母對應哪個字母找回來

然後就可以對應回去原本的樣子再做 base59 decode

`TWCTF{67ced5346146c105075443add26fd7efd72763dd}`

# other write-ups and resources

