n = int(input())
memo = [0] * (n+1)

def make_one(n):

    for i in range(2,n+1):
        memo[i] = memo[i-1]+1

        if i%2==0:
            memo[i] = min(memo[i],memo[i//2]+1)
        if i%3==0:
            memo[i] = min(memo[i],memo[i//3]+1)    

    return memo[n]

print(make_one(n))