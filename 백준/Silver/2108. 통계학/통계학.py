from collections import Counter
import sys
def _many(_list):

    common = Counter(_list).most_common() 

    k = []
    f=common[0][1]

    for i in range(len(common)):
        if common[i][1]==f:
            k.append(common[i])
        else:
            break

    if len(k)==1:
        return k[0][0]
    else:
        return k[1][0]

n = int(sys.stdin.readline().strip())
nums = []

for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    nums.append(tmp)
nums.sort()


avg = round(sum(nums)/n)

cen = nums[n // 2]

minu = nums[-1] - nums[0]

#print(nums)
l = len(nums)
print(avg)
print(cen)
print(_many(nums))
print(minu)