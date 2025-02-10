from collections import deque

n,k = map(int,input().split())

ans = deque()
for i in range(1,n+1):
    ans.append(i)

res = []
while 1:
    for i in range(0,k-1):
        tmp = ans.popleft()
        #print(tmp)
        ans.append(tmp)
    tmp2 = ans.popleft()
    res.append(tmp2)
    if len(ans)==0:
        break

print("<",end="")
for i in range(len(res)-1):
    print(str(res[i])+',',end=" ")
print(str(res[-1])+'>')