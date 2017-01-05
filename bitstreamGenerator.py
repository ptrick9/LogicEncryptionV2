import random

def bitStream(filename, numInp, rows):
    while True:
        try:
            f = open(filename, 'w')
            for i in range(rows):
                t = random.getrandbits(numInp)
                t = bin(t)[2:]
                #f.write(t.zfill(numInp) + '\n')
                f.write(str(i) + ": " + t.zfill(numInp) + '\n')
                #print(t.zfill(numInp))
            f.close()
            break
        except:
            print('caught!')
            pass

#bitStream('test.pat', 36, 10)