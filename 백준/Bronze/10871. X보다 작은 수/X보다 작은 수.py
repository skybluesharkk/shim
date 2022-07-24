N,X = map(int,input().split())
k=list(map(int,input().split()))

for i in range(N):
    if X>k[i]:
        print(k[i],end=" ")
    else:
        pass