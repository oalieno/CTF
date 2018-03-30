# VolgaCTF QUALS 2018 : CrackMe

**category** : reverse

**points** : 100

**solves** : 82

## write-up

給的執行檔是 .NET 的東東

用 dotPeek 做 decompile

觀察一下可以發現他是 AES CBC 的加解密

但是他的 key generation 有問題

中間有幾個 if else 都是恆真式 (ex : ~(x & y) == (~x | ~y)) 

簡化之後發現不管一開始 key generation 的 input 是什麼出來的 key 都是 4 組一樣的 4 bytes (ex : JEDIJEDIJEDIJEDI)

也就是暴搜所需要的複雜度降到 2^32 = 4294967296

所以就暴搜下去就好了

p.s. 我記得其實一組 4 bytes 的小 key 的最左跟最右的 bit 是 0 ( 當時看到是四組一樣的小 key 就直接開 multithread 暴力跑下去了 )

# other write-ups and resources

* https://github.com/DancingSimpletons/writeups/blob/master/volgactf-2018/CrackMe.ipynb
