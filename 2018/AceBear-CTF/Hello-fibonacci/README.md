# AceBear CTF 2018 : Hello fibonacci?

**category** : crypto
**points** : 100

> Yesterday, my friend shows me some math sequence.
>
> And now, it's your turn to showed me your skill.
>
> No vuln, just math, raw math :3
>
> Service: nc 35.200.176.244 8856
>
> Mirror: nc 13.115.164.244 6856

## write-up

有一個變形的費式數列 `fn = fn-1 + fn-3`

前幾項是 `3 2 1 4 6 7 ...`

給 `n` 和 `N` 求 `fn % N`

寫出關係式用矩陣乘法表示

![](https://i.imgur.com/qpDuQZs.png)

![](https://i.imgur.com/941Cuc0.png)

然後就用矩陣快速冪

時間複雜度 : `O(log(N))`

完全就是 ACM 題目阿

## other write-ups and resources

* https://ctftime.org/writeup/8571
