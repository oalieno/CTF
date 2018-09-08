# noxCTF 2018 : Chop-Suey

**category** : crypto

**points** : 118

**solves** : 235

## write-up

I guess e = 65537 and solve it at first glance XD

We can also use dp and dq to reconstruct d ( chinese remainder theorem )

But notice that `(p - 1)` and `(q - 1)` has a common factor 4, can't directly use chinese remainder theorem

See the code for more detail

`noxCTF{W31c0m3_70_Ch1n470wn}`

# other write-ups and resources

