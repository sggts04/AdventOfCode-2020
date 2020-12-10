import sys

path = []

for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

i=0
trees1 = 0
for line in path:
    if line[i]=='#':
        trees1+=1
    i = (i + 1)%len(line)

i=0
trees2 = 0
for line in path:
    if line[i]=='#':
        trees2+=1
    i = (i + 3)%len(line)

i=0
trees3 = 0
for line in path:
    if line[i]=='#':
        trees3+=1
    i = (i + 5)%len(line)

i=0
trees4 = 0
for line in path:
    if line[i]=='#':
        trees4+=1
    i = (i + 7)%len(line)

i=0
j=0
trees5 = 0
while j<len(path):
    line = path[j]
    if line[i]=='#':
        trees5+=1
    i = (i + 1)%len(line)
    j += 2

print(trees1 * trees2 * trees3 * trees4 * trees5)