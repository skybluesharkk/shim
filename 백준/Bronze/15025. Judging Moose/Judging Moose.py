l,r = map(int,input().split())
a=[]
a.append(l)
a.append(r)
if l==0 and r ==0:
    print('Not a moose')
elif (l==r):
    print('Even',l*2)
elif (l!=r):
    print('Odd',max(a)*2)
else:
    pass