
'''
dp
bottom-up 방식으로 문제를 푼다.

맨마지막 계단은 무조건 밟아야 하므로 그 전에 어디서 출발해서 그 계단을 밟았는지 보는게 좋을것 같다

n번째를 밟았을 때

n-1번째에서 오는 경우가 있고
    dp(n-3)+stairs[n-1]+stairs[n]
n-2번째에서 오는 경우가 있다.
    dp[n-2]+stairs[n]

이 두가지 경우 중에서 더 큰것을 선택한다고 보면 된다.

'''
n = int(input())
stairs = [0]*301

for i in range(1,n+1):
    stairs[i] = int(input())

dp = [0] * 301

dp[1]=stairs[1]
dp[2]=stairs[1]+stairs[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[n])

