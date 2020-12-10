import sys

dp = []

def rec(nums, i, last):
    global dp
    if dp[i][last]!=-1:
        return dp[i][last]
    if nums[i] - last <= 3:
        if i+1 == len(nums)-1:
            dp[i][last] = 1
        else:
            dp[i][last] = rec(nums, i+1, nums[i]) + rec(nums, i+1, last)
    else:
        dp[i][last] = 0
    return dp[i][last]

nums = []

for line in sys.stdin:
    line = line.rstrip()
    nums.append(int(line))

nums.sort()

mx = nums[len(nums)-1]
nums.append(mx+3)

for i in range(200):
    a = []
    for j in range(200):
        a.append(-1)
    dp.append(a)

ans = rec(nums, 0, 0)

print(ans)
