a,b,c = map(int,input().split())
d = []
d.append(a)
d.append(b)
d.append(c)
e = sorted(d)

if a==b==c:
    print(10000+1000*a)
elif (a==b)and(b!=c):
    print(1000+100*a)
elif (b==c)and(c!=a):
    print(1000 + 100 * b)
elif (a==c)and(b!=a):
    print(1000 + 100 * c)
else:
    print(e[-1]*100)