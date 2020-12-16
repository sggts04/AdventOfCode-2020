import sys

h = {}
k = 0
err = 0
for line in sys.stdin:
    line = line.rstrip()
    if line=='':
        k+=1
        continue
    if k==0:
        em = line.split(':')
        field = em[0]
        ne = em[1][1:].split(' ')
        valrange1 = int(ne[0].split('-')[0])
        valrange2 = int(ne[0].split('-')[1])
        valrange3 = int(ne[2].split('-')[0])
        valrange4 = int(ne[2].split('-')[1])
        i = valrange1
        while i<=valrange2:
            h.update({i: True})
            i+=1
        i = valrange3
        while i<=valrange4:
            h.update({i: True})
            i+=1
    if k==1:
        if line.startswith('your'):
            continue
        # my ticket
    if k==2:
        if line.startswith('nearby'):
            continue
        fields = line.split(',')
        for field in fields:
            if int(field) in h:
                continue
            else:
                err += int(field)

print(err)
