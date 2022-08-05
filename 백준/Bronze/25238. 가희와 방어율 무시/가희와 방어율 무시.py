a, b = map(int, input().split())

c = a-(a*b*(0.01))

if 100<=c:
    print('0')
else:
    print('1')