n=int(input())
c,b=map(int,input().split())
t = int(c//2)+b
if t>n:
    print(n)
elif t==n:
    print(n)
else:
    print(t)