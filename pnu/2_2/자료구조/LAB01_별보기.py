city = [[0 for x in range(500)] for y in range(500)]

n = int(input())

for i in range(n):
    s,h,w = map(int,input().split())
    for j in range(s,s+w+1):
        for k in range(0,h+1):
            city[499-k][j]=1

nstar = int(input())

for i in range(nstar):
    xstar,ystar=map(int,input().split())
    if city[499-ystar][xstar] == 0 and city[499-ystar-1][xstar] == 0:
        print('over')
    elif city[499-ystar][xstar] == 1 and city[499-ystar-1][xstar] == 0:
        print('on')
    elif city[499-ystar][xstar] == 1 and city[499-ystar][xstar+1] == 0:
        print('on')
    elif city[499-ystar][xstar] == 1 and city[499-ystar][xstar-1] == 0:
        print('on')
    elif city[499-ystar][xstar] == 1 and city[499-ystar-1][xstar] == 1:
        print('under')
    else:
        pass

for i in range(len(city)):            # 세로 크기
    for j in range(len(city[i])):     # 가로 크기
        print(city[i][j], end=' ')
    print()
