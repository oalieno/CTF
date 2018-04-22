# VXCTF 2018 : Multiprime RSA

**category** : crypto

**points** : 500

**solves** : 1

## write-up

```
x = getPrime(1024)
n = x * next_prime(2 * x) * next_prime(2 * next_prime(2 * x)) * next_prime(2 * next_prime(2 * next_prime(2 * x)))
```

直接二分搜 x 再反解明文就好了

# other write-ups and resources

