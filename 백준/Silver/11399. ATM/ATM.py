import sys
n = int(input())

nums = sys.stdin.readline().split()

for i in range(len(nums)):
    nums[i]=int(nums[i])


nums.sort()
ans=0
for i in range(len(nums)):
    ans+=nums[i]*(len(nums)-i)

print(ans)