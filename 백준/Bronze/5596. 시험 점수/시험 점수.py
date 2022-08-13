a,b,c,d = map(int,input().split())
s=a+b+c+d
q,w,e,r = map(int,input().split())
t=q+w+e+r
v=[]
v.append(s)
v.append(t)
v.sort()
print(v[1])