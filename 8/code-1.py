import sys

path = []
accu = 0
vis = []
for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

for line in path:
    vis.append(False)

i = 0
while i<len(path):
    if vis[i]:
        print(accu)
        break
    else:
        vis[i] = True
    line = path[i]
    cmd, val = line.split(' ')
    if cmd=='nop':
        i+=1
    elif cmd=='acc':
        accu += int(val)
        i+=1
    else:
        i += int(val)