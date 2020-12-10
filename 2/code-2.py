from sys import stdin

c=0
for line in stdin:
    a = line
    min = int(a.split('-')[0])
    max = int(a.split('-')[1].split(' ')[0])
    x = a.split(' ')[1][0]
    passw = a.split(':')[1][1:]
    cou = 0
    if passw[min-1]==x:
        cou+=1
    if passw[max-1]==x:
        cou+=1
    if cou==1:
        c+=1
print(c)
