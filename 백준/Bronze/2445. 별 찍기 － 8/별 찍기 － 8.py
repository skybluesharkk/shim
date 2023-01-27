n = int(input())
for i in range(1,n):
    print('*'*(i)+' '*(2*n-(2*i))+'*'*i)
for j in range(n,0,-1):
    print('*'*(j)+' '*(2*n-(2*j))+'*'*j)