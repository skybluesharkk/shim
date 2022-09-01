a,b,c = map(int, input().split())
d = []
d.append(a)
d.append(b)
d.append(c)
j=0; k=0
for i in range(3):
    if d[i]==1:
        j+=1
    if d[i]==2:
        k+=1
if j>k:
    print(1)
else:
    print(2)