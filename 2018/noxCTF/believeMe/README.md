# noxCTF 2018 : believeMe

**category** : pwn

**points** : 378

**solves** : 90

## write-up

The vulnerability is format string

There is a secret function called `noxFlag` that can give us the flag

Since no aslr, find out the return address on remote server, and overwrite return address to `noxFlag`

`noxCTF{%N3ver_%7rust_%4h3_%F0rmat}`

# other write-ups and resources

