a,b = map(int,input().split())
d = []
sum=0
for i in range(1,b+1):
    for j in range(i):
        d.append(i)

d = d[a-1:b]

for k in range(len(d)):
    sum+=d[k]
print(sum)