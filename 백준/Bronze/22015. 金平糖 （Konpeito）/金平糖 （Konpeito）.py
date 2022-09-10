a,b,c=map(int,input().split())
d=[]
d.append(a)
d.append(b)
d.append(c)
d.sort()
if a == b == c:
    print(0)
else:
    print(max(d)*2-d[0]-d[1])