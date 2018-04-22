# VXCTF 2018 : Classical Medley

**category** : crypto, reverse

**points** : 500

**solves** : 1

## write-up

這題有兩小題

其實不難，只是原始碼寫的看起來很複雜

第一題就是 : affine cipher (f(x) = ax + b (mod n))

我們知道明文前面是 `vxctf{` 那就直接反求 a, b 就套回去就好了

第二題是 : 每九個字做一次 permutation cipher (就是把順序攪亂)

我們知道明文前面是 `vxctf{` 那就找回 permutation 的順序再套回去就好了

這題就是要耐心看個程式碼 O_O

# other write-ups and resources

