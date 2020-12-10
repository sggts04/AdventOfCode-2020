import sys

nums = []
path = []
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
            print(n)
            break