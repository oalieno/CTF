#!/usr/bin/env python
import struct

word = "AIS3"
word_int = struct.unpack("I",word)[0]

keys = [964600246,1376627084,1208859320,1482862807,1326295511,1181531558,2003814564]

secret = keys[0]^word_int

ans = ""

for i in xrange(1,7):
    ans += struct.pack("I",secret^keys[i])

print ans
