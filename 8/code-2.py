import sys

path = []
accu = 0
for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

j = 0
while j<len(path):
    cmd1, val1 = path[j].split(' ')
    if cmd1=='nop':
        path[j] = 'jmp ' + val1
    elif cmd1=='jmp':
        path[j] = 'nop ' + val1
    else:
        j+=1
        continue
    
    accu=0
    vis = []
    for line in path:
        vis.append(False)

    mi = 0
    done = False
    i = 0
    while i<len(path):
        mi = max(mi, i)
        if vis[i]:
            if mi==653:
                print(accu)
                print(mi)
                print()
            done = True
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
            if int(val)==0:
                break
    
    if not done:
        print(accu)
        print(mi)
        print()

    if cmd1=='nop':
        path[j] = 'nop ' + val1
    elif cmd1=='jmp':
        path[j] = 'jmp ' + val1
    
    j+=1