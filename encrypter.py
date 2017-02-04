import re
from circuit import *
#GPK = Key inputs
#GPI = Normal inputs


#def encrypt(filename, net):
def encrypt(C, net, replacements):



    newInput = 'INPUT(keyinput%i)' % (C.keyCounter + 1)
    C.addLine(newInput)

    ##print(C.dump())

    if '->' in net:
        nets = net.split(' ')[0].split('->')
        #print(nets)

        inp = False
        for val in C.inputs:
            if nets[0] in val:
                inp = True
                break


        i = 0
        while i < len(C.gates):
            if C.gates[i].split(' ')[0] == nets[0]:
                #print(C.gates[i])
                s = "GGATEK%i = XOR(%s, keyinput%i)" % (C.GATECounter + 1, nets[0], C.keyCounter)
                C.gates.insert(i+1, s)
                i += 1
                #print(s)
            elif nets[0] in C.gates[i] and nets[1] in C.gates[i]:
                #print("---" + C.gates[i] + "---- %s" % (nets))
                s = C.gates[i]
                s = s.replace(nets[0], "GGATEK%i" % (C.GATECounter + 1))
                #print(s)
                C.gates[i] = s

            i += 1

        if inp:
            s = "GGATEK%i = XOR(%s, keyinput%i)" % (C.GATECounter + 1, nets[0], C.keyCounter)
            C.gates.insert(0, s)

    else:
        nets = net.split(' ')[0]
        #print(nets)

        inp = False
        outs = False
        for val in C.inputs:
            if nets in val:
                inp = True
                break
        for val in C.outputs:
            if nets in val:
                outs = True
                break


        i = 0
        while i < len(C.gates):
            if C.gates[i].split(' ')[0] == nets:
                #print(C.gates[i])
                s = "GGATEK%i = XOR(%s, keyinput%i)" % (C.GATECounter + 1, nets, C.keyCounter)
                C.gates.insert(i+1, s)
                i += 1
                ##print(s)
            elif nets in C.gates[i]:
                #print("---" + C.gates[i] + "---- %s" % (nets))
                s = C.gates[i]
                s = s.replace(nets, "GGATEK%i" % (C.GATECounter + 1))
                ##print(s)
                C.gates[i] = s

            i += 1

        if inp:
            s = "GGATEK%i = XOR(%s, keyinput%i)" % (C.GATECounter + 1, nets, C.keyCounter)
            C.gates.insert(0, s)
        if outs:
            print('woo boy, we got an output')
            i = 0
            replacements['GGATEK%i' % (C.GATECounter + 1)] = nets
            while i < len(C.outputs):
                if nets in C.outputs[i]:
                    C.outputs[i] = 'OUTPUT(GGATEK%i)' % (C.GATECounter + 1)
                    break
                i += 1

            print(nets)
            #s = "GGATEK%i = XOR(%s, GPK%i)" % (C.GATECounter + 1, nets, C.keyCounter)
            #C.gates.insert(0, s)
    C.GATECounter = C.GATECounter + 1
    #print(C.dump())
    #return C.dump()



#encrypt('c432_test.bench', 'GGATE135 /1')
#encrypt('c432_test.bench', 'GGATE83->GGATE87 /0')
#encrypt('c432_test.bench', 'GPI4->GGATE94 /1')