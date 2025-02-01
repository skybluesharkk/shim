n = int(input())

memo = [0]
memo.append(1)
memo.append(1)

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        for i in range(2,n+1):
            tmp = memo[-1]+memo[-2]
            memo.append(tmp)

    return memo[n]

print(fibo(n))
#print(memo)