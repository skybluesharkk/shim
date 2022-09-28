p1,s1 = map(int,input().split())
s2,p2 = map(int,input().split())

P = p1+p2
S = s1+s2
if P>S:
    print('Persepolis')
elif P == S:
    if s1>p2:
        print('Esteghlal')
    elif s1==p2:
        print('Penalty')
    else:
        print('Persepolis')
else:
    print('Esteghlal')