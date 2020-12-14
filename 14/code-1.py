import sys

mask = ''
dict = {}
for line in sys.stdin:
    line = line.rstrip()
    if line.startswith('mask'):
        mask = line.split(' ')[2]
    else:
        addr = int(line.split('[')[1].split(']')[0])
        val = int(line.split(' ')[2])
        binval = '{:036b}'.format(val)
        newval = ''
        i=0
        while i<36:
            if mask[i]=='X':
                newval += binval[i]
            else:
                newval += mask[i]
            i+=1
        dict.update({addr: newval})

sum = 0
for key in dict.keys():
    val = dict[key]
    sum += int(val, 2)

print(sum)