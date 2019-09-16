# CSAW CTF Qualification Round 2019 : Byte Me

**category** : crypto

**points** : 50

**solves** : 100

## write-up

This challenge doesn't have source code

```
2a1bdfb7ebbe650f321ce2a77a04dd5ecd5e8e01d76199ecc1e297aed8c55e7f0a27082856274b313c0fa172325ef8fb367df56cc99a51012c141999b71aa805
Tell me something: a
a
6ee608a947872f083d1e4daa999b8838fb7cddcc836ea190c901b8d07939b0674e9a066d0fbf50eea7046e8d79ad550377c175d3a5eb5bd2b8cc80cac5a778f0
Tell me something: aa
aa
c620a8a963feef6b2505c07b8ed133ef01eb5054f8995613af1bb72735d422fa31d36f35cbe863898ea16650e75100d4755ed5a9832bf96d1b7bbd3101deed44
```

Server will give us some hash depending on our input

After some time of trying and guessing, I figure out that the source code should looks like this

```python
def block_hash(data):
    ans = b''
    for i in range(0, len(data), 16):
        ans += hash(data[i:i+16])
    return ans

block_hash(salt + user_input + flag)
```

The length of salt is unknown, so we need to find out the length of salt first

Then we can retrieve the flag character by character ( see source code for more detail )

flag: `flag{y0u_kn0w_h0w_B10cks_Are_n0T_r31iab13...}`

# other write-ups and resources
