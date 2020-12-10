import sys

nums = []
path = []
ans = 0
for line in sys.stdin:
    line = line.rstrip()
    path.append(line)

for line in path:
    if len(nums) < 25:
        nums.append(int(line))
    else:
        n = int(line)
        i=0
        done = False
        while i<len(nums):
            j = i+1
            while j<len(nums):
                if nums[i]+nums[j]==n:
                    done = True
                    break
                j+=1
            if done:
                break
            i+=1
        if done:
            nums.pop(0)
            nums.append(n)
        else:
            ans = n
            break

done = False
i = 0
while i<len(path):
    j = i
    sum = 0
    while j<len(path):
        sum += int(path[j])
        if sum > ans:
            break
        if sum==ans:
            done = True
            break
        j+=1
    if not done:
        i+=1
        continue
    else:
        mi = int(path[i])
        ma = int(path[i])
        c = i
        while c<=j:
            mi = min(mi, int(path[c]))
            ma = max(ma, int(path[c]))
            c+=1
        print(mi, ma)
        print(mi + ma)
        break

