memo = [0] * 1001
memo[1] = 1

n = int(input())

if n>=2:
    memo[2] = 3
    for i in range(3,n+1):
        memo[i] = (memo[i-2]*2)+memo[i-1]
print(memo[n]%10007)