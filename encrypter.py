import re
from circuit import *
#GPK = Key inputs
#GPI = Normal inputs


def encrypt(filename, net):
    f = open(filename, 'r')
    C = Circuit()
    keyCounter = 1
    patt = re.compile('\d+')
    for line in f:
        if 'GPK' in line:
            print(line)
            num = int(patt.findall(line)[0])
            if num > keyCounter:
                keyCounter = num
        C.addLine(line)
    print(C)

    newInput = 'INPUT(GPK%i)' % (keyCounter + 1)
    C.addLine(newInput)


    print(C.dump())


encrypt('c432_test.bench', 'GGATE135 /1')
encrypt('c432_test.bench', 'GGATE83->GGATE87 /0')