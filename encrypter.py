import re
from circuit import *
#GPK = Key inputs
#GPI = Normal inputs


def encrypt(filename, net):
    f = open(filename, 'r')
    C = Circuit()
    keyCounter = 0
    GATECounter = 0
    patt = re.compile('\d+')
    for line in f:
        if 'GPK' in line:
            #print(line)
            num = int(patt.findall(line)[0])
            if num > keyCounter:
                keyCounter = num
        if 'GGATEK' in line and 'XOR' in line and 'GPK' in line:
            num = int(patt.findall(line)[0])
            if num > GATECounter:
                GATECounter = num
        C.addLine(line)
    #print(C)

    newInput = 'INPUT(GPK%i)' % (keyCounter + 1)
    C.addLine(newInput)

    ##print(C.dump())

    if '->' in net:
        nets = net.split(' ')[0].split('->')
        #print(nets)

        i = 0
        while i < len(C.gates):
            if C.gates[i].split(' ')[0] == nets[0]:
                #print(C.gates[i])
                s = "GGATEK%i = XOR(%s, GPK%i)" % (GATECounter + 1, nets[0], keyCounter + 1)
                C.gates.insert(i+1, s)
                i += 1
                #print(s)
            elif nets[0] in C.gates[i] and nets[1] in C.gates[i]:
                #print("---" + C.gates[i] + "---- %s" % (nets))
                s = C.gates[i]
                s = s.replace(nets[0], "GGATEK%i" % (GATECounter + 1))
                #print(s)
                C.gates[i] = s

            i += 1

    else:
        nets = net.split(' ')[0]
        #print(nets)
        i = 0
        while i < len(C.gates):
            if C.gates[i].split(' ')[0] == nets:
                #print(C.gates[i])
                s = "GGATEK%i = XOR(%s, GPK%i)" % (GATECounter + 1, nets, keyCounter + 1)
                C.gates.insert(i+1, s)
                i += 1
                ##print(s)
            elif nets in C.gates[i]:
                #print("---" + C.gates[i] + "---- %s" % (nets))
                s = C.gates[i]
                s = s.replace(nets, "GGATEK%i" % (GATECounter + 1))
                ##print(s)
                C.gates[i] = s

            i += 1
    #print(C.dump())
    return C.dump()



#encrypt('c432_test.bench', 'GGATE135 /1')
#encrypt('c432_test.bench', 'GGATE83->GGATE87 /0')