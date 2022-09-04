time = int(input())
d = []
for i in range(time):
    a,b = map(int,input().split())
    if a<=b:
        d.append(b)
    else:
        pass
d.sort()
if len(d)==0:
    print(-1)
else:
    print(d[0])