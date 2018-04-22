import random
import math
from Cipher import Substitution, Generalized_Affine
from FLAG import flag, flag2

print "######################Stage 1#######################"

print "Lets break substitution cipher!"
n = random.randint(2,2**32)
print "n: {}".format(n)
    
S = Substitution(n)

print "Ciphertext: {}".format(S.encrypt(flag))

print "######################Stage 2#######################"

print "Lets break generalized Affine cipher now!"

print "n: {}".format(n)

G = Generalized_Affine(n,int(math.ceil(math.sqrt(len(flag2)))))

print "Ciphertext: {}".format(G.encrypt(flag2))

