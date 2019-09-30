# BSides Delhi CTF 2019 : ExtendedElgamal

**category** : crypto

**points** : 964

## write-up

`rand = lambda: random.randint(133700000,2333799999)` this is a small range  
Brute force it and get `z`  
Then calculate `e / (g^k)^z` to get `m`

flag: `bsides_delhi{that5_som3_b4d_k3y_generation!}`

# other write-ups and resources
