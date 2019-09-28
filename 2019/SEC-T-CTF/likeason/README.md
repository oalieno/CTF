# SEC-T CTF 2019 : likeason

**category** : crypto

**points** : 1337

**solves** : 1

## write-up

I didn't solve this challenge during the contest.

This challenge is yet another rsa oracle, but the oracle only give us `bin(m).count('1') & 0x1`

It can still be solved using the same old technique, LSB Oracle Attack, only a little different

We send message `2 ** (0 * e) * c, 2 ** (1 * e) * c, ...` and get the bit count parity of `2 ** 0 * m, 2 ** 1 * m, ...`

There are two circumstances:
1. If the bit count parity is change, we are sure that there must be an overflow over n.
2. If the bit count parity is unchange, we know nothing ( just like John Snow )

### First Method

From the LSB Oracle Attack point of view:
1. If the bit count parity is change, `L = (L + U) // 2`
2. If the bit count parity is unchange, both of `L = (L + U) // 2` and `U = (L + U) // 2` are possible to happend, we need to try both possibilities.
3. Then we prune the path using the fact that the character set only contains `'.-'`

### Second Method

From the Bleichenbacher 1998 point of view:

If the bit count parity is change between `2 ** (s - 1) * m, 2 ** s * m`, then we have the following condition:

```
let x = (2 ** (s - 1) * m) % n
0 <= x < n
n <= 2 * x < 2 * n
```

Simplified a bit, we get:

```
let k = (2 ** (s - 1) * m - 2 ** (s - 1) * m % n) / n
(k + 1/2) * n / 2 ** (s - 1) <= m < (k + 1) * n / 2 ** (s - 1)
(2 ** (s - 1) * m - n) / n < k <= (2 ** (s - 1) * m - n * 1/2) / n
```

Try all possible k to get many possible intervals of m, and union all intervals.  
Everytime you will reduce the possible range of m, and finally get an interval of size 1 which is flag.  
We also can prune out the intervals using the fact that the character set only contains `'.-'`

The performance of the second method is worth than the first one, maybe due to massive amount of union on intervals?

By the way, I use sage with python3

# other write-ups and resources
