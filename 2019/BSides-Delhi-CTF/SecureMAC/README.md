# BSides Delhi CTF 2019 : SecureMac

**category** : crypto

**points** : 871

## write-up

Two parts in this challenge:
1. get the key
2. generate a collision to this mac

### First Part

Same technique as in [CSAW CTF - Fault Box](https://github.com/OAlienO/CTF/tree/master/2019/CSAW-CTF/Fault-Box)

let `f` be `bytes_to_long("fake_flag")`  
`c` will be `f ** e + k * p` for some `k`  
We know the value of `f ** e`  
Simply calculate `gcd(f ** e - c, n)` will give us prime factor `p`, then we can factor `n`

### Second Part

To make things simple, we send messages of 32 bytes.  
Both `messageblocks[1]` and `tag`, which is `ECB.encrypt(messageblocks[0])` we can control  
Just make the result of `strxor` be the same

flag: `bsides_delhi{F4ult'n'F0rg3_1s_@_b4d_c0mb1n4ti0n}`

# other write-ups and resources
