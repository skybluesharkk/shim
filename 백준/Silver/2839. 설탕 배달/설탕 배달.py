n = int(input())

# 5x+3y=18
ans = []
for i in range(n//5 +1):
    for j in range(n //3 +1):
        if (5*i+3*j)==n:
            ans.append(i+j)
if len(ans)==0:
    print(-1)
else:
    print(min(ans)) 
