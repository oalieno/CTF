#!/usr/bin/env python3
import string
from enigma.machine import EnigmaMachine

'''
for a in string.ascii_uppercase:
    for b in string.ascii_uppercase:
        for c in string.ascii_uppercase:
            for d in ['B', 'C', 'B-Thin', 'C-Thin']:
                machine = EnigmaMachine.from_key_sheet(
                   rotors = 'I II III',
                   reflector = d,
                   ring_settings = '{} {} {}'.format(a, b, c),
                   plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
                )
                result = machine.process_text('IPUXZGICZWASMJFGLFVIHCAYEGT', replace_char='$')
                if result.startswith('HOWDY'):
                    print(result)
                    print(a, b, c, d)
'''

machine = EnigmaMachine.from_key_sheet(
   rotors = 'I II III',
   reflector = 'B',
   ring_settings = 'T C O',
   plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
)
print(machine.process_text('LTHCHHBUZODFLJOAFNNAEONXPLDJQVJCZPGAVOLN', replace_char='$'))
