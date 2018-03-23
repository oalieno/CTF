#!/usr/bin/env python

public = "040201010701010105020101050101000402010104020101"
secret = "10001c04041f1f010a151c110a1f2c4304051b010f010c39"

public = [ int(public[i:i+2],16) for i in xrange(0,len(public),2) ]
secret = [ int(secret[i:i+2],16) for i in xrange(0,len(secret),2) ]

p = (17,34,51,68)

flag = [ chr(public[i]*p[i%4]+secret[i]) for i in xrange(len(public)) ]

print "".join(flag)
