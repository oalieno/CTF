# N1CTF 2018 : rsa padding

**category** : crypto
**points** : 303
**solves** : 47/517

## write-up

經典的 Franklin-Reiter Related Message Attack

相同 N 相同 e 且 m1 = f(m2)

因為我們知道並且可以操控 padding

所以被加密的明文 m1, m2 可以用多項式 f 轉換

反正就 Franklin-Reiter Related Message Attack 炸下去就對了

小心 c1, c2 不要放反了

flag : N1CTF{f7efbf4e5f5ef78ca1fb9c8f5eb02635}

## other write-ups and resources

