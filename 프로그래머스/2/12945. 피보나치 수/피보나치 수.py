def solution(n):
    if n == 0:
        return 0
    fibo = [0] * (n + 1)
    fibo[1]=1
    fibo[2]=1
    for i in range(2,n+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
    #print(fibo[:n+1])
    #print(fibo[n])
    answer = fibo[n]%1234567
    return answer