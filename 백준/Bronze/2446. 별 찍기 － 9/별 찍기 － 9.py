n = int(input())
for i in range(n):
    print(' '*(i)+'*'*(2*n-(2*i+1)))
for j in range(n-2,-1,-1):
    print(' '*(j)+'*'*(2*n-(2*j+1)))