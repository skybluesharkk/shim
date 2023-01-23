def fact(a):
    _sum=1
    for i in range(1,a+1):
        _sum*=i
    return _sum

n,k = map(int,input().split())

print(int((fact(n))/((fact(k))*(fact(n-k)))))