#!/usr/bin/env python

with open("leg.txt") as d:
    data = d.read().strip()

script = "syms"

for i in xrange(84):
    script += " a{}".format(i)

script += ';\n'

for index,line in enumerate(data.split('\n')):
    var = line.split(" == ")[0]
    number = line.split(" == ")[1]
    script += "eqn{} = ".format(index)
    for v in var.split(" + "):
        v = v.partition('[')[2].partition(']')[0].strip()
        script += "a{} + ".format(v)
    script = script.rstrip(" + ") + " == " + str(number) + ";\n"

script += '['

for i in xrange(84):
    script += "A{},".format(i)

script = script.rstrip(',') + '] = solve(['

for i in xrange(84):
    script += "eqn{},".format(i)

script = script.rstrip(',') + "]);"

with open("script.m","w") as d:
    d.write(script)
