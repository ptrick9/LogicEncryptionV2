from circuit import *
import re

def createFaultList(circ):
    #patt = re.compile('\d+')
    f = open('faults.flt', 'w')
    for gate in circ.gates:
        g = gate.split(' ')[0]
        sa0 = g + ' /0\n'
        sa1 = g + ' /1\n'
        f.write(sa0)
        f.write(sa1)
    f.close()





