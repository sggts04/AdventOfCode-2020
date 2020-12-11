import sys

bigpath = []

def checkAdj(i ,j):
    global bigpath
    i+=1
    j+=1
    c = 0
    if bigpath[i-1][j-1]=='#':
        c+=1
    if bigpath[i-1][j]=='#':
        c+=1
    if bigpath[i][j-1]=='#':
        c+=1
    if bigpath[i+1][j+1]=='#':
        c+=1
    if bigpath[i+1][j]=='#':
        c+=1
    if bigpath[i][j+1]=='#':
        c+=1
    if bigpath[i+1][j-1]=='#':
        c+=1
    if bigpath[i-1][j+1]=='#':
        c+=1
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


for _ in range(101):
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
                if a>=4:
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
        if seat=='#':
            s+=1

print(s)