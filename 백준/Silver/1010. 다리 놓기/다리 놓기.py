
def factorial(n):
    j=1
    for i in range(1,n+1):
        j=j*i
    return j

#print(factorial(5))

def combi(a,b):
    res = factorial(b)/(factorial(a)*factorial(b-a))
    return res
num = int(input())

for k in range(num):
    a,b = map(int,input().split())
    print(int(combi(a,b)))