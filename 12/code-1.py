import sys

path = []
ang = 0
ew = 0
ns = 0
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
        ang = (ang + val)%360
    if ac=='R':
        ang = (ang - val)%360
    if ac=='F':
        if ang==90:
            ns+=val
        if ang==270:
            ns-=val
        if ang==0:
            ew+=val
        if ang==180:
            ew-=val

print(abs(ew)+abs(ns))