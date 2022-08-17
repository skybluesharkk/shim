a,b = map(int,input().split())
c = [int(x) for x in input().strip().split()]
for i in range(5):
    print(c[i]-a*b, end=" ")