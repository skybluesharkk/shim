a = list(map(int,input().split()))

for i in range(len(a)):
    for j in range(len(a)-1-i):
        if (a[j]<=a[j+1]):
            tmp=a[j]
            a[j]=a[j+1]
            a[j+1]=tmp
print(a[1])