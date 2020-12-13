import sys

nums = []
time = 0
i=0
for line in sys.stdin:
    line = line.rstrip()
    if i==0:
        time = int(line)
        i+=1
    else:
        nums = [int(x) for x in line.split(',') if x!='x']

ear=99999999
minb = 0

for num in nums:
    an=0
    div = time//num
    if time%num==0:
        an=div
    else:
        an = div+1
    early = num*an
    if early < ear:
        ear = early
        minb = num

print(ear-time, minb, (ear-time)*minb)