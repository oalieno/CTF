# HITCON CTF 2018 : Lost-Modulus

**category** : crypto

**points** : 230

**solves** : 42

## write-up

It's a paillier cryptosystem

We can do encryption and decryption

But decryption only give us the last byte

Observe that `dec(enc(m)) = m % n`, we can set `m = (1 << i)` for `i = range(1024, 7, -1)` to binary search `n`

For the last byte, `(known_m + 0x100) % n = (m % 0x100)`

We still have 14 operations to used

Because the homomorphic properties, we can do minus and divide to `flag >> 8` and get the next byte of flag

Flag will not change, so just do many times and wait for it to leak the flag

flag : `hitcon{binary__search__and_least_significant_BYTE_oracle_in_paillier!!}`

# other write-ups and resources

