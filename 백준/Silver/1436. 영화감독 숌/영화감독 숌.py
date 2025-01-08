n = int(input())

ans = []
ccnt = n

k=666
while 1:
    if k==666:
        ans.append(k)
    elif '666' in str(k):
        ans.append(k)
    else:
        pass
    k+=1
    if len(ans)==ccnt:
        break

print(ans[n-1])