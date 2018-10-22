# HITCON CTF 2018 : Lost-Key

**category** : crypto

**points** : 257

**solves** : 29

## write-up

It's a RSA cryptosystem

We also have encryption and decryption oracles as in `Lost-Modulus` challenge

But the decryption only give us the last byte

It's looks like a classic `LSB Oracle Attack`, but without `n` and `e`

First, we can leak `n = gcd(enc(2) ** 2 - enc(2 ** 2), enc(3) ** 2 - enc(3 ** 2))`

Don't need to leak `e`, leak `enc(256) = 256 ** e % n` will be enough

Then we will do Least Significant **Byte** Oracle Attack

Assume `n % 256 == 1`

And use `dec(enc(256) * enc(flag)) = (256 * flag) % n` to reduce the possible range of `flag` as in the original Least Significant Bit Oracle Attack

If `n % 256 != 1`, just run again XD ( 1/128 possibility, because n is odd number )

flag : `hitcon{1east_4ign1f1cant_BYTE_0racle_is_m0re_pow3rfu1!}`

# other write-ups and resources

