from collections import Counter

def _many(_list):

    common = Counter(_list).most_common() 

    #print(common)
    k = []
    f=common[0][1]
    #print(f)
    for i in range(len(common)):
        if common[i][1]==f:
            k.append(common[i])
    #print(f, common[f][0])
    #print(common)
    #print(k)
    if len(k)==1:
        return k[0][0]
    else:
        return k[1][0]

n = int(input())
nums = []

for i in range(n):
    tmp = int(input())
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