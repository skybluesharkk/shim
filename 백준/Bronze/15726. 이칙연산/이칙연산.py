a,b,c = map(int,input().split())
d=[]
d.append(int(a*b/c))
d.append(int(a/b*c))
d.sort()
print(d[1])