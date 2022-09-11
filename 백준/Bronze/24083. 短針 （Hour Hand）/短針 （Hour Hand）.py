a = int(input())
b = int(input())

c = b%12
if (a+c)>12:
    print(a+c-12)
else:
    print(a+c)