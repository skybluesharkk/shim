from collections import deque

n = int(input())

ans = deque([i for i in range(1,n+1)])

while len(ans)!=1:
    ans.popleft()
    #tmp=ans.pop(0)
    #ans.pop(0)
    #print(tmp,ans)
    ans.append(ans.popleft())
print(ans[0])