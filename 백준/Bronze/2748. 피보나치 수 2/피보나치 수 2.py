n = int(input())

memo = [0] * 45
memo[1] = 1

def fibo(n):
    k=0
    j=1
    ans=[]
    ans.append(k)
    ans.append(j)
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        for i in range(1,n):
            tmp = ans[-1]+ans[-2]
            ans.append(tmp)
            #print(i,k,j,tmp)
            #print(ans)
    return tmp

print(fibo(n))
