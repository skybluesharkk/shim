n = int(input())
ans = []
summ=0
for i in range(n):
    a = int(input())
    if (i==0):
        ans.append(a)
    else:
        if (a==0):
            ans.pop()
        else:
            ans.append(a)
if (len(ans)==0):
    summ=0
else:
    for j in range(len(ans)):
        summ+=ans[j]
print(summ)