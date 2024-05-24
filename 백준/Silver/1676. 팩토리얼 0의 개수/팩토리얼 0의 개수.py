def factorial(n):
    cnt=1
    for i in range(1,n+1):
        cnt = cnt* i
    return cnt

#print(factorial(5))

def make_list(n):
    res = []
    while n>10:
        key = n%10
        n = n // 10
        res.append(key)
    res.append(n)
    return res
#print(make_list(factorial(5)))

def find_non_zero(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i]==0:
            cnt+=1
        else:
            break
    return cnt


num = int(input())
print(find_non_zero(make_list(factorial(num))))

