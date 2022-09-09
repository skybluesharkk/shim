n,m,k = map(int,input().split())

if k==m:
    print(n)
elif k>m:
    print(m+n-k)
else:
    print(k+n-m)