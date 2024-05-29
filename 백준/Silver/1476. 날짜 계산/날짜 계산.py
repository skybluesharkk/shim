import sys

e,s,m = map(int,sys.stdin.readline().strip().split())

'''
음 100년이라고 치면
15까지는

15 15 15

16년은

1 16 16

17년

2 17 17
3 18 18
4 19 19
5 20 1
6 21 2
7 22 3
8 23 4
9 24 5
10 25 6
11 26 7
12 27 8
13 28 9
14 1 10

그냥 for 문 돌릴까?
규칙을 만들고 -> 예를 들면 if문으로 구현해서
for문안에서 계속 하다가 원래 꺼랑 같아지는 즉시 탈출 + 해당 순번 출력
으로 구현하면 안되나

일단 해보고 시간초과되면 다시 해보자.
'''
e_,s_,m_ = 1,1,1
i = 0

for j in range(7980):
    #print(i)
    i+=1
    e_+=1
    s_+=1
    m_+=1
    if e_>=16:
        e_=1
    if s_>=29:
        s_=1
    if m_>=20:
        m_=1
    if e==e_ and s==s_ and m==m_:
        break

if e==1 and s==1 and m==1:
    print(1)
else:
    print(i+1)
