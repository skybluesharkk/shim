a,b=map(int,input().split())
d = []
d.append(a-b)
d.append(a+b)
print(max(d))
print(min(d))