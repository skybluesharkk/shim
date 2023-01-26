n = int(input())
ans_a=[]
for j in range(n):
    a = int(input())
    ans_a.append(a)

for i in range(len(ans_a)-1):
    for j in range(len(ans_a)-1-i):
        if (ans_a[j]>=ans_a[j+1]):
            tmp=ans_a[j]
            ans_a[j]=ans_a[j+1]
            ans_a[j+1]=tmp
for i in range(len(ans_a)):
    print(ans_a[i])