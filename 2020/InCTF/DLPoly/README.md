# InCTF 2020 : DLPoly

**category** : crypto

**points** : 676

## write-up

```python
P.<x> = PolynomialRing(Zmod(p))
Q.<x> = QuotientRing(P, P.ideal(n))
g = x
print(bsgs(g, gX, (0, 2 ^ 56), operation='*'))
```

Use sagemath `bsgs` ( baby step giant step ) to brute force discrete logarithm.  
But may run out of memory. I split it into 1024 sections and run each section paralleling using 8 core.  
See `a.sh` and `b.sh` and `solve.sage` for details.  
And then found that the length of flag is only 13 !??

## flag

`inctf{bingo!}`

# other write-ups and resources
