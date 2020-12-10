import sys

path = []

for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

a = set()
count = 0
for line in path:
    if line=='':
        count += len(a)
        a = set()
    for c in line:
        a.add(c)

count += len(a)
a = set()
print(count)
    