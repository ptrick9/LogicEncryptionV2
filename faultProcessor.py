import operator

def faultProcessor(faultFile, outputFile, currentCounter):
    if(len(currentCounter.keys()) < 1):
        fault = open(faultFile, 'r')
        for line in fault:
            line = line.rstrip()
            currentCounter[line] = 0
    output = open(outputFile, 'r')
    outFaults = []
    lines = []
    for line in output:
        lines.append(line.rstrip())
    i = 0
    j = 0
    while i < len(lines):
        #print(lines[i])
        if 'test' in lines[i]:
            #print(lines[i])
            if i > j:
                outFaults.append(lines[j:i])
                j = i
        i += 1
    outFaults.append(lines[j:i])
    for test in outFaults:
        #print(test)
        correct = test[0].split(' ')[-1]
        #print(correct)
        for vector in test[1:]:
            if '*' in vector:
                fOut = vector.split(' ')[-1]
                count = sum(1 for a, b in zip(correct, fOut) if a != b)
                fName = vector.split(':')[0].lstrip()
                #print('%s %s %s %i' % (fName,correct, fOut, count))
                currentCounter[fName] = currentCounter[fName] + count
    sorted_counter = sorted(currentCounter.items(), key = operator.itemgetter(1))
    sorted_counter.reverse()
    #print(sorted_counter[-1])
    bigFault = ''
    #bigFault = sorted_counter[0]
    #'''
    for val in sorted_counter:
        #print(val)
        if 'K' not in val[0]:
            bigFault = val
            break
    #'''
    return currentCounter, bigFault
    #


#faultProcessor('faults.flt', 'outs.ou', {})