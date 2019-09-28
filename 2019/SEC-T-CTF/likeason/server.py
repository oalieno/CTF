#! /usr/bin/env python
import sys

from secret import d, n


def oracle(c, x=1):
    res = bin(pow(c, d * x, n)).count('1') & 0x1
    return int(res)


while True:
    try:
        c = [int(x) for x in sys.stdin.readline().split(" ")]
        if len(c) == 1:
            sys.stdout.write("%d\n" % oracle(c[0]))
        else:
            sys.stdout.write("%d\n" % oracle(c[0], x=c[1]))
    except Exception:
        sys.stdout.write("Nope.\n")

    sys.stdout.flush()

# e = 0x10001
# c = 32028315366572316530941187471534975579021238700122793819215559206747120150118490538115208229905399038122261293920013020124257186389163654867911967899754432511568776857320594304655042217535057811315461534790485879395513727264354857833013662037825295017832478478693519684813603327210332854320793948700855663229
