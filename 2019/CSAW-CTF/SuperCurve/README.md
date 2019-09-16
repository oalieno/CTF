# CSAW CTF Qualification Round 2019 : SuperCurve

**category** : crypto

**points** : 300

**solves** : 171

## write-up

This is a trivial challenge

`secret_scalar = random.randrange(curve.order)` the order here is just 7919

brute force `secret_scalar` and get the flag

flag: `flag{use_good_params}`

# other write-ups and resources
