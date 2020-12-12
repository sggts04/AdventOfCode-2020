import sys

path = []
ang = 0
ew = 10
ns = 1
sew = 0
sns = 0
for line in sys.stdin:
    line = line.rstrip()
    ac = line[0]
    val = int(line[1:])
    if ac=='N':
        ns+=val
    if ac=='S':
        ns-=val
    if ac=='E':
        ew+=val
    if ac=='W':
        ew-=val
    if ac=='L':
        val = val%360
        if val==90:
            ew, ns = -ns, ew
        if val==180:
            ew = -ew
            ns = -ns
        if val==270:
            ew, ns = ns, -ew
    if ac=='R':
        val = val%360
        if val==90:
            ew, ns = ns, -ew
        if val==180:
            ew = -ew
            ns = -ns
        if val==270:
            ew, ns = -ns, ew
    if ac=='F':
        sew = sew + val*ew
        sns = sns + val*ns

print(abs(sew)+abs(sns))