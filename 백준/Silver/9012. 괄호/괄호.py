a = int(input())
l=0
r=0
for i in range(a):
    l=0
    ans=list(input())
    #print(ans)
    for j in range(len(ans)):
        if (ans[j]=='('):
            l+=1
        else:
            l-=1
        if (l<0):
            print('NO')
            break
        if (j==len(ans)-1)and(l==0):
            print('YES')
        if (j==len(ans)-1)and(l!=0):
            print('NO')
        #print(j,l)