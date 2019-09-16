# CSAW CTF Qualification Round 2019 : Brillouin

**category** : crypto

**points** : 500

**solves** : 39

## write-up

This challenge use Boneh–Lynn–Shacham Scheme for signature verification

You can read [this article](https://medium.com/cryptoadvance/bls-signatures-better-than-schnorr-5a7fe30ea716) first

In line 66, the server didn't check the third public key, so we can forge a public key here

Read the source code of `bls.scheme.aggregate_vk` [here](https://github.com/asonnino/bls/blob/master/bls/scheme.py#L54)

First `chester_sign` to sign a valid signature `s` of 'this stuff'

Send `s` and `2 * s` as signatures to server

Forge the third public key to cancel the second public key and make the `aggregate_vk` calculate to `publics[2] + 2 * publics[2]`

Becuase the `Threshold` is True, it is actually calculate to `l2[0] * publics[2] + l2[1] * 2 * publics[2]`

flag: `flag{we_must_close_the_dh_gap}`

# other write-ups and resources
