# TokyoWesterns CTF 5th 2019 : M-Poly-Cipher

**category** : crypto

**points** : 279

**solves** : 26

## write-up

After some reverse engineering, we found some matrix multiplication operations

Assume the following:  
```
R, PK1, PK2, PK3, PT are 8x8 matrix
R is randomly generated 8x8 matrix
PK1, PK2, PK3 are 3 Public Key
PT is Plain Text
```

The encryption data is (0x300 bytes):  
```
R x PK1
R x PK2
R x PK3 + PT
```

All operations are under modular 0xFFFFFFFB

All we need to do is solve the equations R x PK1 and R x PK2 for R ( see code for more detail )  
After we have R, subtract R x PK3 from R x PK3 + PT and get the flag

flag: `TWCTF{pa+h_t0_tomorr0w}`

# other write-ups and resources
