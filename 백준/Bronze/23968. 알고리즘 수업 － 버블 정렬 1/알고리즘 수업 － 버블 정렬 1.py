import sys
n,k = map(int,input().split())

ans = list(map(int, sys.stdin.readline().split()))


cnt=0
y = len(ans)
for i in range(y-1):
    change = False
    for j in range(y-1-i):
        if (ans[j]>ans[j+1]):
            ans[j], ans[j+1] = ans[j+1],ans[j]
            cnt+=1
            change = True
            if (cnt==k):
                print(ans[j],ans[j+1])
                break
    if (cnt==k) or (change==False):
        break

if (cnt<k):
    print(-1)