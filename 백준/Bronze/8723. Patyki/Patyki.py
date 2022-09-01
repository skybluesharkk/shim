a,b,c = map(int, input().split())
d = []
d.append(a)
d.append(b)
d.append(c)

d.sort()
if d[0]==d[1]==d[2]:
    if (d[2])**2==(d[1]**2)+(d[0]**2):
        print(1)
    else:
        print(2)
elif (d[2])**2==(d[1]**2)+(d[0]**2):
    print(1)
else:
    print(0)
