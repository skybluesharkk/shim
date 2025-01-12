n = int(input())

ans = []
for i in range(n):
    c,d = map(int,input().split())
    ans.append([c,d])

res = []
tmp=0

for j in range(len(ans)):
    for k in range(len(ans)):
        if j==k:
            pass
        else:
            if ans[j][0]<ans[k][0] and ans[j][1]<ans[k][1]:
               tmp+=1
    res.append(tmp+1)
    tmp=0

for i in range(len(res)):
    if i!=len(res)-1:
        print(res[i],end=" ")
    else:
        print(res[i])