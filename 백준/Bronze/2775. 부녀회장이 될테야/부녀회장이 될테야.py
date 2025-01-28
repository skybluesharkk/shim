
p = int(input())

for i in range(p):
    k = int(input())
    n = int(input())
    memo = [j for j in range(1,n+1)] 

    for i in range(1,k+1):
        for j in range(1,n):
            memo[j] +=memo[j-1]
    print(memo[-1])
