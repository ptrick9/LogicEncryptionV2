from bitstreamGenerator import bitStream
from faultProcessor import *
from encrypter import encrypt
import subprocess
from time import sleep
from circuit import *
from createFaultList import createFaultList

#command = "cmd.exe atalanta-M -S -t c432.pat -P c432.rep -m c432.msk c432.bench"
#command = ['cmd.exe']
'''
createFaultList = ['atalanta-M', '-F', 'faults.flt', 'c432_2.bench']
createOutputs = ['hope', '-f', 'faults.flt', '-F', 'outs.ou', '-t', 'test.pat', '-l', 'c432.dict', '-N', '-D', 'c432_3.bench']

proc = subprocess.Popen(createFaultList).wait()
bitStream('test.pat', 37, 100)
proc = subprocess.Popen(createOutputs).wait()
sleep(.05)
c, m = faultProcessor('faults.flt', 'outs.ou', {})
print(c)
print(m)
'''
'''f = open('c432.msk', 'r')
l = f.readline()
f.close()
print(str(i) + ": " + l)
sleep(.05)'''


circ = Circuit()
circ.buildFromFile('encryptedFiles/c432_0.bench')
keyedGates = []
replacements = {}

for i in range(35):
    #createFaultList = ['atalanta-M', '-F', 'faults.flt', 'encryptedFiles/c432_%i.bench' % (i)]
    createOutputs = ['hope', '-f', 'faults.flt', '-F', 'outs.ou', '-t', 'test.pat', '-l', 'c432.dict', '-N', '-D', 'encryptedFiles/c432_%i.bench' % (i)]
    print(circ.keyCounter)
    #proc = subprocess.Popen(createFaultList).wait()
    createFaultList(circ)
    #break
    bitStream('test.pat', 36+i, 1000)
    proc = subprocess.Popen(createOutputs, shell=False, stdout=subprocess.PIPE).wait()
    sleep(.05)
    c, m = faultProcessor2('faults.flt', 'outs.ou', {}, keyedGates)
    #print(c)
    print(m[0])
    #break
    #circ = encrypt('encryptedFiles/c432_%i.bench' % (i), m[0])
    encrypt(circ, m[0], replacements)

    encrypted = open('encryptedFiles/c432_%i.bench' % (i+1), 'w')
    for line in circ.dump():
        encrypted.write(line)
    encrypted.close()
print(i)
print(replacements)

encryptedCircuit = open('c432_encrypted.bench', 'w')

for line in circ.dumpArray():
    for k in replacements:
        #print("%s %s" % (k, line))
        if str(k) in line:
            print("%s %s" % (k, line))
            line = line.replace(k, "%s$enc" % (replacements[k]))
            print("%s %s" % (k, line))
    encryptedCircuit.write(line + "\n")
encryptedCircuit.close()
