n = int(input())
for i in range(n):
    print(' '*(n-i-1)+'*'*((2*i+1)))
for j in range(1,n):
    print(' '*j+'*'*(2*n-(2*j+1)))