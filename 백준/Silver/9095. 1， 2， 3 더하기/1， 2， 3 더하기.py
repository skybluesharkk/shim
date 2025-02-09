dp = [0] * 20
dp[1]=1
dp[2]=2
dp[3] = 4
dp[4]=7

n = int(input())
for i in range(n):
    a = int(input())

    if a<=4:
        print(dp[a])
    else:
        for j in range(4,a+4):
            dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
        print(dp[a])
#print(dp)