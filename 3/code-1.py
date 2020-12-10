import sys

path = []

for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

i=0
trees = 0
for line in path:
    if line[i]=='#':
        trees+=1
    i = (i + 3)%len(line)

print(trees)