#  Teaser Dragon CTF 2018 : AES-128-TSB

**category** : crypto

**points** : 219

**solves** : 46

## write-up

![](https://i.imgur.com/Zy3HJ0S.png)

The problem implement a new kind of AES mode

It check the last decrypt block equal to IV

There are two things we can use in `server.py` 

1. `unpad`: `msg[:-ord(msg[-1])]`
2. `a == b`: It compares string for us after decryption

First, how to bypass the check for mac

Observe that `P2 = IV + j1 + j2`

We just need to make `j1 == j2`, which is the same as `i1 == i2`

Second, we can alter the last bit of `P1` using IV last bit, and compare the string with empty string

If `1 <= P1[-1] <= 15` then the unpad P1 will not be an empty string, otherwise it will be an empty string.

Using above method, we can recover last bit of `j1`

Since we know last bit of `j1`, we can unpad any bytes we want through manipulating last bit of IV.

Brute force `0-255` to compare with each byte in `j1` ( just make first 15 bytes of IV `\x00` )

After get a `i1` and `j1` pair, we can make `gimme_flag` string

Then recover the encrypted flag using the same method

Because there are many requests, and the network is slow, it takes about an hour to get the flag...

`DrgnS{Thank_god_no_one_deployed_this_on_production}`

# other write-ups and resources

