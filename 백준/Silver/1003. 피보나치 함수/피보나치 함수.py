def fibo(n):
    zeros = [1,0,1]
    ones = [0,1,1]
    if n <=2:
        print(zeros[n],ones[n])
    else:
        for i in range(3,n+1):
            zeros.append(zeros[i-1]+zeros[i-2])
            ones.append(ones[i-1]+ones[i-2])
        print(zeros[n],ones[n])


t = int(input())

for i in range(t):
    tmp = int(input())
    fibo(tmp)
