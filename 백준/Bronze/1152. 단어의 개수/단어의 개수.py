import sys

a = sys.stdin.readline()

b = list(a)
b.remove('\n')
if (len(b)==1) and (b[0]==' '):
    print(0)
elif (len(b)==1) and (b[0]!=' '):
    print(1)
else:
    if (b[0]==" "):
        b.pop(0)
    if (b[-1]==" "):
        b.pop()
    if (len(b)==1):
        print(1)
    else:
        cnt=0
        for i in range(len(b)):
            if (i==0):
                pass
            if (((b[i-1]!=" ")and (b[i]==' '))or i==len(b)-1):
                cnt+=1
            else:
                pass
        print(cnt)