import sys

nums = []

for line in sys.stdin:
    line = line.rstrip()
    nums.append(int(line))

nums.sort()
one = 0
three = 0

last = 0
for num in nums:
    diff = num - last
    if diff == 1:
        one+=1
    elif diff==3:
        three+=1
    last = num

three+=1

print(one * three)