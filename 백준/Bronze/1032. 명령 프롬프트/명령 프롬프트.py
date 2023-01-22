a = int(input())

d = []
for i in range(a):
    b = list(input())
    if(i==0):
        d=b
    else:
        pass
    for j in range(len(d)):
        if (d[j]!=b[j]):
            d[j]='?'


for j in range(len(d)):
    if (j!=len(d)-1):
        print(d[j],end="")
    else:
        print(d[j])