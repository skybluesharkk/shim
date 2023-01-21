a = int(input())
b = int(input())
c = int(input())
x = int(a*b*c)
_x = list(map(int,str(x)))
cnt=0
ans=[]
for i in range(10):
    for j in range(len(str(x))):
        if (i == _x[j]):
            cnt+=1
    ans.append(cnt)
    cnt=0
for i in range(len(ans)):
    print(ans[i])