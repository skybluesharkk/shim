n = int(input())
for i in range(n):
    a = list(map(str,input()))
    for i in range(len(a)):
        if ord(a[i])>=65 and ord(a[i])<=90:
            a[i] = chr(ord(a[i])+32)
        print(a[i],end='')
        if i == len(a)-1:
            print(' ')