import sys

store = {}
mytick = []
nearby = []
h = {}
k = 0

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
        store.update({field: [valrange1, valrange2, valrange3, valrange4]})
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
        mytick = [int(x) for x in line.split(',')]
    if k==2:
        if line.startswith('nearby'):
            continue
        err = False
        fields = [int(x) for x in line.split(',')]
        for field in fields:
            if field in h:
                continue
            else:
                err = True
                break
        if not err:
            nearby.append(fields)

loc = {}

for key in store.keys():
    r11 = store[key][0]
    r12 = store[key][1]
    r21 = store[key][2]
    r22 = store[key][3]
    i=0
    while i<len(mytick):
        done = True
        for ticket in nearby:
            if (ticket[i]>=r11 and ticket[i]<=r12) or (ticket[i]>=r21 and ticket[i]<=r22):
                continue
            else:
                done = False
                break
        ticket = mytick
        if (ticket[i]>=r11 and ticket[i]<=r12) or (ticket[i]>=r21 and ticket[i]<=r22):
            pass
        else:
            done = False
        if not done:
            i+=1
        else:
            if key in loc:
                p = loc[key]
                p.append(i)
                loc.update({key: p})
            else:
                loc.update({key: [i]})
            i+=1

exloc = {}
while len(exloc)<20:
    for key in loc.keys():
        if len(loc[key])==1:
            val = loc[key][0]
            exloc.update({key: val})
            for k in loc.keys():
                p = loc[k]
                p = [x for x in p if x!=val]
                loc.update({k: p})
            break

val = 1
for key in exloc:
    if key.startswith('departure'):
        val = val * mytick[exloc[key]]

print(val)
