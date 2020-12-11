import sys

bigpath = []

def checkAdj(i ,j):
    global bigpath
    i+=1
    j+=1
    c = 0

    #north
    ip = i-1
    while ip>0:
        if bigpath[ip][j]=='L':
            break
        elif bigpath[ip][j]=='#':
            c+=1
            break
        ip-=1
    
    #south
    ip = i+1
    while ip<len(bigpath):
        if bigpath[ip][j]=='L':
            break
        elif bigpath[ip][j]=='#':
            c+=1
            break
        ip+=1

    #east
    jp = j+1
    while jp<len(bigpath[0]):
        if bigpath[i][jp]=='L':
            break
        elif bigpath[i][jp]=='#':
            c+=1
            break
        jp+=1
    
    #west
    jp = j-1
    while jp>0:
        if bigpath[i][jp]=='L':
            break
        elif bigpath[i][jp]=='#':
            c+=1
            break
        jp-=1

    #northeast
    ip = i-1
    jp = j+1
    while jp<len(bigpath[0]) and ip>0:
        if bigpath[ip][jp]=='L':
            break
        elif bigpath[ip][jp]=='#':
            c+=1
            break
        ip-=1
        jp+=1

    #northwest
    ip = i-1
    jp = j-1
    while jp>0 and ip>0:
        if bigpath[ip][jp]=='L':
            break
        elif bigpath[ip][jp]=='#':
            c+=1
            break
        ip-=1
        jp-=1
    
    #southeast
    ip = i+1
    jp = j+1
    while jp<len(bigpath[0]) and ip<len(bigpath):
        if bigpath[ip][jp]=='L':
            break
        elif bigpath[ip][jp]=='#':
            c+=1
            break
        ip+=1
        jp+=1

    #southwest
    ip = i+1
    jp = j-1
    while jp>0 and ip<len(bigpath):
        if bigpath[ip][jp]=='L':
            break
        elif bigpath[ip][jp]=='#':
            c+=1
            break
        ip+=1
        jp-=1

    return c

path = []

for line in sys.stdin:
    line = line.rstrip()
    path.append(list(line))

lin = []
for i in range(len(path[0])+2):
    lin.append('.')
bigpath.append(lin)
for line in path:
    nlin = line[:]
    nlin.insert(0, '.')
    nlin.append('.')
    bigpath.append(nlin)
bigpath.append(lin)


for _ in range(102):
    i=0
    while i<len(path):
        j = 0
        while j<len(path[i]):
            seat = path[i][j]
            if seat == 'L':
                a = checkAdj(i, j)
                if a==0:
                    path[i][j] = '#'
            elif seat=='#':
                a = checkAdj(i, j)
                if a>=5:
                    path[i][j] = 'L'
            j+=1
        i+=1

    i=0
    while i<len(path):
        j=0
        while j<len(path[i]):
            bigpath[i+1][j+1] = path[i][j]
            j+=1
        i+=1


s=0
for line in path:
    for seat in line:
        print(seat, end='')
        if seat=='#':
            s+=1
    print()

print(s)