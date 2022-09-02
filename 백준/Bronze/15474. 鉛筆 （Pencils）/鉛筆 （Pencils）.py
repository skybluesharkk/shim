n,a,a1,b,b1 = map(int,input().split())

A = n%a
B = n%b

if A==0:
    _a = (n//a)*a1
else:
    _a = (n//a+1)*a1
if B==0:
    _b = (n//b)*b1
else:
    _b = (n//b+1)*b1

if _a>=_b:
    print(_b)
else:
    print(_a)