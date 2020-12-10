import sys

#path = []
ans = -1
seats = []
minans = 100000

for line in sys.stdin:
    line = line.rstrip()
    st = 0
    en = 127
    row = line[:7]
    for c in row:
        mid = int((st + en)/2)
        if c=='F':
            en = mid
        else:
            st = mid+1
    
    col = line[7:]
    st2 = 0
    en2 = 7
    for c in col:
        mid = int((st2 + en2)/2)
        if c=='L':
            en2 = mid
        else:
            st2 = mid+1
    print(st, en, st2, en2)
    ans = max(ans, en * 8 + en2)
    minans = min(minans, en * 8 + en2)
    seats.append(en * 8 + en2)

for i in range(minans, ans):
    if i not in seats:
        print(i)
