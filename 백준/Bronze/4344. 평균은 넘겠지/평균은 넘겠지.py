c = int(input())

nums = [list(map(int, input().split())) for _ in range(c)]

#print(nums)
sum=0
avg=0
uup=0
for i in range(len(nums)):
    for j in range(1,len(nums[i])):
        sum+=nums[i][j]
    avg = sum/nums[i][0]
    #print(avg)
    for k in range(1,len(nums[i])):
        if (nums[i][k]>avg):
            uup+=1
    uup/=nums[i][0]
    print(str(f'{uup*100:.3f}'+'%'))
    avg=0
    sum=0
    uup=0