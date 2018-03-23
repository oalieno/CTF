#!/usr/bin/env python
import angr
import claripy

project = angr.Project("./break", auto_load_libs = False)

state = project.factory.entry_state()

for _ in range(100):
    c = state.posix.files[0].read_from(1)
    state.solver.add(c <= '~')
    state.solver.add(c >= ' ')

state.posix.files[0].seek(0)

simgr = project.factory.simgr(state)
simgr.explore(find = 0x40091f, avoid = 0x400831)
print(simgr)
print(simgr.found[0].posix.dumps(0))
