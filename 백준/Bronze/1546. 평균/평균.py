a = int(input())
b = list(map(int,input().split(" ")))
#print(a)
#print(b)
M = max(b)
#print(M)
for i in range(len(b)):
        b[i] = (b[i]/M)*100

#print(b)
cnt=0
for i in range(len(b)):
    cnt+=b[i]
print(cnt/len(b))