# UIUCTF 2017 : PapaRSA

**category** : crypto

**points** : 250

**solves** : 6

## write-up

我是參考下面那篇 writeups 做的

第一次用真的用 coppersmith's method 來做題目

coppersmith's method 簡而言之就是可以找 monic polynomial modulo N 的 small root ( monic 就是最高次方項係數為 1 )

root x 滿足 x < N ^ (1/degree(f(x)) - epsilon) 就可以算是 small root

epsilon 我們可以自己取值，所以 x 最多到 N ^ 1/degree(f(x)) 都可以算 small root

這題我們就是已知大部分明文

f(x) = (message + 2^792 * x) ^ e - C

未知明文的長度是 60 bytes = 480 bits

所以 x < 2 ^ 480

所以 x ^ degree(f(x)) = x < 2 ^ 480 < (2 ^ 4096) ^ (1/5) = 2 ^ 819.2

我們可以使用 coppersmith's method 來解題

coppersmith's method 在 sage 叫做 small_roots

並且預設的 epsilon 是 1/8

那我們的 epsilon 要設多少呢

2 ^ 480 < (2 ^ 4096) ^ (1/5 - epsilon)

0.1171875 < 1/5 - epsilon

epsilon < 1/5 - 0.1171875 = 0.0828125

1/epsilon > 12.075471698113208

那我們就設 1/13 就可以囉

# other write-ups and resources

* https://hgarrereyn.gitbooks.io/th3g3ntl3man-ctf-writeups/content/2017/UIUCTF/problems/Cryptography/papaRSA/
