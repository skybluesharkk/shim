from collections import deque

import sys
n,m = map(int,sys.stdin.readline().strip().split())
nums = []

nums = list(map(int,sys.stdin.readline().strip().split()))

#print(nums)
nums.sort()
nums.reverse()
#print(nums)
cnt=0
sum=0
ans = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = nums[i]+nums[j]+nums[k]
            #print(nums[i],nums[j],nums[k])
            if sum > m:
                continue
            else:
                ans.append(sum)
print(max(ans))