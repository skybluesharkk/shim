m,n = map(int,input().split())
ans=n
for i in range(m):
    a ,b = map(int,input().split())
    ans+=a
    ans-=b
print('비와이')