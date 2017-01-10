from bitstreamGenerator import bitStream
from faultProcessor import faultProcessor
import subprocess
from time import sleep

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

createFaultList = ['atalanta-M', '-F', 'faults.flt', 'encryptedFiles/c432.bench']
createOutputs = ['hope', '-f', 'faults.flt', '-F', 'outs.ou', '-t', 'test.pat', '-l', 'c432.dict', '-N', '-D', 'encryptedFiles/c432.bench']

proc = subprocess.Popen(createFaultList).wait()
bitStream('test.pat', 36, 100)
proc = subprocess.Popen(createOutputs).wait()
sleep(.05)
c, m = faultProcessor('faults.flt', 'outs.ou', {})
print(c)
print(m)

