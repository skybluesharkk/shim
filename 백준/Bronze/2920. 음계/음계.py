a = list(map(int,input().split()))
b = sorted(a)
c = reversed(b)

if (a==b):
    print('ascending')
elif (a==list(c)):
    print('descending')
else:
    print('mixed')