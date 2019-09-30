# BSides Delhi CTF 2019 : BabyRSA

**category** : crypto

**points** : 930

## write-up

This is yet another RSA challenge  
`salt` can be decrypt directly  
Then, use wiener attack to factor `n = p * q` and get `p1 * p2`  
Simply gcd `p1 * p2` with `n1` and `n2` and get all the prime factors  
Note that `gcd(e1, (p1 - 1) * (q1 - 1)) != 1` and `gcd(e2, (p2 - 1) * (q2 - 1)) != 1`, we can't directly decrypt `magic`  
Luckily, `gcd(e1, q1 - 1) == 2` and `gcd(e2, q2 - 1) == 2`  
We can get `m ** 2 % q1` and `m ** 2 % q2`  
Then use the same technique as in Rabin cryptosystem, which is modular square root and chinese remainder theorem

flag: `bsides_delhi{JuG1iNg_WiTh_RS4}`

# other write-ups and resources
