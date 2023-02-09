import math

m,n=map(int,input().split())

def is_prime_number(n):
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array
ans = is_prime_number(n)
for i in range(m, n+1):
    if ans[i]:
        if (i!=1):
            print(i)