a = int(input())

for i in range(a):
    t = int(input())
    for j in range(t):
        a,b = map(int,input().split())
        print(a+b,a*b)