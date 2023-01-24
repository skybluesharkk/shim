a,b = map(int,input().split())
numa = []
numb = []

rans=[]

_min=0
for i in range(1,a+1):
    if (a%i==0):
        numa.append(i)
for i in range(1,b+1):
    if (b%i==0):
        numb.append(i)

if (len(numa)>=len(numb)):
    ans=numb
    nans=numa
else:
    ans=numa
    nans=numb
for k in range(len(ans)):
    if (ans[k] in nans):
        rans.append(ans[k])
_min = max(rans)
print(_min)
part_a=a/_min
part_b=b/_min
print(int(part_a*part_b*_min))