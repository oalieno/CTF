# DEFCON CTF Qualifier 2020 : ooo-flag-sharing

**category** : crypto

**points** : 135

**solves** : 36

## TL;DR

Binary search on `if secret.startswith(b"OOO{"):`

## write-up

This challenge is about secret sharing scheme

`reconstitute_secret` takes out 5 rows from the matrix according to the index in the provided shares. Then inverse the matrix and dot product the first row with the shares to get the secret. Since we only cares about secret, other rows in inverse matrix is not important. In other words, `reconstitute_secret` takes 5 shares and dot product with a vector of size 5. Just like this `a_1 * s_1 + a_2 * s_2 + a_3 * s_3 + a_4 * s_4 + a_5 * s_5`. All operation is done under modulus `P`.

`redeem_actual_flag` will decrypted the actual flag from 3 shares we provided and 2 shares in the server and check that it starts with "OOO{". That sounds like some oracle attack!!! Assume the shares we provided is `s_3, s_4, s_5`. Instead of `s_5`, we use `s_5 + x * a_5^-1` with arbitrary `x` to feed to oracle. We will get `flag + x`. `flag` is stored in little endian, so "OOO{" is in the lower bits. Making an arbitrary `x << 32` and observe that how big the value of `x << 32` will make `flag + (x << 32)` overflow to be modulus by `P` and invalid the check. That means to binary search for `x` such that `flag + (x << 32) == P`.

Next question is how do we get `a_5`. `redeem_user_flag` can do reconstitute and give us the actual value of secret. Set the values of shares to `0, 0, 0, 0, 1` to extract the value.

Because the shares is being random shuffle, we also need know the index of the `secret_id.1` and `secret_id.2` in order to extract the same inverse matrix. This can be done by simply brute force these two index, which has only `(100 - 1 - 2) * (100 - 1 - 2)` possibilities. And test whether `flag + (1 << 32)` still valid.

## flag

`OOO{ooo_c4nt_ke3p_secr3ts!}`

# other write-ups and resources
