a,b,c = map(int, input().split())
d = ((b-a)%c)
if d == 0:
    print(((b-a)//c))
elif d>0:
    print(((b-a)//c)+1)
else:
    pass