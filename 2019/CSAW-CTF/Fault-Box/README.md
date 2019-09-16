# CSAW CTF Qualification Round 2019 : Count On Me

**category** : crypto

**points** : 400

**solves** : 108

## write-up

`TEST_CRT_encrypt` can be simplified to

```
for arbitrary k, m is fake flag
c = c2 + q * (qinv * (c1 - c2) % p)
c = c2 + (kp + q % p) * (qinv * (c1 - c2) % p)
c = c2 + ((c1 - c2) % p) + kp
c = c1 % p + kp
c = m ** e % p + kp
```

So we know that `gcd(n, m ** e - c) = kp`

`x, y` are generated from `gen_prime` offset, and is very small

Finally, brute force against the fake flag and factor n using gcd

flag: `flag{ooo000_f4ul7y_4nd_pr3d1c74bl3_000ooo}`

# other write-ups and resources
