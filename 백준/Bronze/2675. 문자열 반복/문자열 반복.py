n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    a = int(a)
    tmp=""
    for j in range(len(b)):
        for k in range(a):
            tmp+=b[j]
    print(tmp)