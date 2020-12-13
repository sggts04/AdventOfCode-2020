import sys
from functools import reduce

# chinese remainder theorem copy pasted
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
# ends


nums = []
n=[]
a=[]
offset = {}
time = 0
i=0
for line in sys.stdin:
    line = line.rstrip()
    if i==0:
        time = int(line)
        i+=1
    else:
        off = line.split(',')
        p=0
        while p<len(off):
            k = off[p]
            if k!='x':
                offset.update({p: int(k)})
            p+=1

for key in offset.keys():
    n.append(offset[key])
    a.append( (-key) % offset[key] )

print(chinese_remainder(n, a))