n = int(input())

ans=[]

for i in range(n):
    a = input()
    if a not in ans:
        ans.append(a)

ans.sort()
ans.sort(key=len)
for k in range(len(ans)):
    print(ans[k])