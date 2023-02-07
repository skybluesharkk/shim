import sys

n,k = map(int, sys.stdin.readline().split())
ans = list(map(int, sys.stdin.readline().split()))
answer = -1
cnt=0
y = len(ans)
for i in range(y-1):

    for j in range(y-1-i):
        if (ans[j]>ans[j+1]):
            ans[j], ans[j+1] = ans[j+1],ans[j]
            cnt+=1

            if (cnt==k):
                answer = f'{ans[j]} {ans[j+1]}'
print(answer)