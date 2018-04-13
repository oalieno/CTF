# UIUCTF 2018 : xoracle

**category** : crypto

**points** : 250

**solves** : 19

## write-up

這題的題目很短但是很有趣

連上 server 後會得到用一把長度 128 - 255 字元範圍是 0 - 255 的 key 作 xor cipher 過的 flag

首先，只拿到一個密文我們不知道他的 key 長度

沒關係，我們可以測試兩個密文 c, d 是不是有相同的 key 長度

我們嘗試所有的 key 長度去檢查

c[0] ^ c[klen] 是不是等於 d[0] ^ d[klen]
c[0] ^ c[klen * 2] 是不是等於 d[0] ^ d[klen * 2]
...

c[1] ^ c[1 + klen] 是不是等於 d[1] ^ d[1 + klen]
c[1] ^ c[1 + klen * 2] 是不是等於 d[1] ^ d[1 + klen * 2]
...

他們一定要相等因為 key 如果是對的，等式兩邊的 key 都會被消掉剩下 m[0] ^ m[klen] 是不是等於 m[0] ^ m[klen]

所以我們現在可以測試兩個密文是不是有相同的 key 長度

那我們就去抓一堆密文，讓他們兩兩比較有沒有相同長度的 key

根據生日勃論我們大約在 sqrt(2ln(2) * 128) 約等於 13 個密文就有 50 % 機會找到相同長度 key 的密文

多收集幾組已知 key 長度的密文

接下來就是暴力嘗試明文的第一個字 m[0]

推出 k[0] = m[0] ^ c[0]

再推出 m[klen] = k[0] ^ c[klen]

記得我們有好幾組不同長度的 key 的密文，有新的明文被解出後也可以推出另一個 key 的某個 byte

最後我們有 256 組可能的明文

用 file 去看他們全部會發現 `m-80:  Zip archive data, at least v2.0 to extract`

解壓縮完有一張 `f.bmp` 裡面就是 flag 啦

# other write-ups and resources

