a,b,c = map(int,input().split())
d = []
d.append(a)
d.append(b)
d.append(c)
d.sort()
print(d[2]+d[1])