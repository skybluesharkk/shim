s = int(input())
#ans set에 안들어가는 경우 while 문 탈출
#탈출하고 cnt에 +1 한 게 정답이 된다.
ans = set()
i=0
cnt=0
nums = 0


'''

한번씩 돌아가면서 세트에 넣는다
첫번째 1
두번째 2
세번째 3
계속해서 남은 숫자의 합을 확인해야 한다.
200
1
2 3
3 6
4 10
5 15
6 21
7 28
8 36
9 45
10 55
11 66
12 78
13 91
14 105
15 120
16 136
17 153
18 171
19 190
20 210
'''
i=0
total=0
while 1:
    i+=1
    total+=i
    cnt+=1
    if total>s:
        print(cnt-1)
        break
    elif total ==s:
        print(cnt)
        break
