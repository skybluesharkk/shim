n = int(input())

for i in range(n):
    sum=0
    count=0
    a = input()
    for j in range(len(a)):
        if a[j]=='O':
            count+=1
            sum+=count
        else:
            count=0
    print(sum)