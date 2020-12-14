import sys
from itertools import chain, combinations

def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

mask = ''
addrs = []
vdict = {}
for line in sys.stdin:
    line = line.rstrip()
    if line.startswith('mask'):
        mask = line.split(' ')[2]
    else:
        addr = int(line.split('[')[1].split(']')[0])
        val = int(line.split(' ')[2])
        binval = '{:036b}'.format(addr)
        newval = ''
        i=0
        while i<36:
            if mask[i]=='0':
                newval += binval[i]
            elif mask[i]=='1':
                newval += '1'
            else:
                newval += 'X'
            i+=1
        addrs.append(newval)
        vdict.update({newval: val})

ndict = {}
sum = 0
for val in addrs:
    toset = vdict[val]
    nval = ''
    x = []
    i=0
    while i<36:
        if val[i]=='X':
            tv = 2**(35-i)
            x.append(tv)
            nval += '0'
        else:
            nval += val[i]
        i+=1
    base_sum = int(nval, 2)
    for subset in all_subsets(x):
        bval = base_sum
        for elem in subset:
            bval += elem
        ndict.update({bval: toset})

for key in ndict.keys():
    sum+=ndict[key]
print(sum)