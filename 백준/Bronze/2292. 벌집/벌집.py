n = int(input())
m=1
cnt=0
while (n>m):
    m=int(1+3*cnt*(cnt-1))
    cnt+=1
    if (n==m):
        print(cnt-1)
        break
if (n!=m):
    if(n!=1):
        print(cnt-1)
if(n==1):
    print(1)