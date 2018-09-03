# TokyoWesterns 2018 : Revolutional-Secure-Angou

**category** : crypto

**points** : 154

**solves** : 82

## write-up

```
e = 65537
p = generate_prime(1024)
q = inverse(e, p)
```

```
eq = kp + 1
p > q
65537 = e > k

en = kp^2 + p
kp^2 + p - en = 0
```

brute force k from 1 to 65537

solve the equation to get p

`TWCTF{9c10a83c122a9adfe6586f498655016d3267f195}`

# other write-ups and resources

