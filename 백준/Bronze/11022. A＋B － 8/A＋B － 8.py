T = int(input())

for i in range(1,T+1):
    a, b = map(int, input().split())
    c = a + b
    print('Case #'+str(i)+':',a,'+',b,'=',c)