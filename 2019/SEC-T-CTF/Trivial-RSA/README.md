# SEC-T CTF 2019 : Trivial RSA

**category** : crypto

**points** : 359

**solves** : 32

## write-up

We are given `n1, n2, (p1 - p2) % (q1 - q2), (q1 - q2) % (p1 - p2), c`, Where

```
n1 = p1 * q1
n2 = p2 * q2
e = 65537
c = pow(m, e, n1)
```

Assume `y1 = (p1 - p2) % (q1 - q2), y2 = (q1 - q2) % (p1 - p2)`  
We already know the values of `y1, y2`  
There are only two possibilities (don't mind the equal situation):  
1. `p1 - p2 < q1 - q2`, then `p1 - p2 = y1, q1 - q2 = y2 + k * y1` for some `k`  
2. `p1 - p2 > q1 - q2`, then `p1 - p2 = y1 + k * y2, q1 - q2 = y2` for some `k`

Brute force the value of `k`, then we know the exact value of `p1 - p2` and `q1 - q2`
Assume the exact values are `p1 - p2 = x1, q1 - q2 = x2`
Then we will have 4 equations

```
p1 - p2 = x1
q1 - q2 = x2
p1 * q1 = n1
p2 * q2 = n2
```

After some math calculations, we will get a quadratic equation

```
x2 * p1 * p1 + (n1 - n2 + x1 * x2) * p1 + x1 * n1 = 0
```

solve for `p1` and factor `n1`

flag: `SECT{ju99lin_w1d_d3m_alg3br0s}`

# other write-ups and resources
