n = int(input())
memo = [0]
memo.append(1)
memo.append(2)
def square(n):
    if n==1:
        #memo[1]=1
        return 1
    if n==2:
        #memo[2]=2
        return 2
    else:
        for i in range(2,n):
            tmp = memo[-1]+memo[-2]
            memo.append(tmp)
    return tmp

print(square(n)%10007)
#print(memo)