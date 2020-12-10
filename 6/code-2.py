import sys

path = []

for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

a = {}
num = 0
count = 0
for line in path:
    if line=='':
        for d in a.values():
            if d==num:
                count+=1
        num=0
        a = {}
        continue
    num+=1
    for c in line:
        if c in a:
            a[c]+=1
        else:
            a[c]=1

for d in a.values():
    if d==num:
        count+=1
num=0
a = {}
print(count)
    