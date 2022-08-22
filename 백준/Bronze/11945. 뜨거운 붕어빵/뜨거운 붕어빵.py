a,b = map(int,input().split())
for i in range(a):
    c = input()
    _c = list(c)
    print(''.join(reversed(_c)))