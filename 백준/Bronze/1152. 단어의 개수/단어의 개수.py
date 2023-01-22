import sys

a = sys.stdin.readline()

#print(a)
#print(type(a))
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
        #print(b)
        cnt=0
        #c=''
        #d=[]
        for i in range(len(b)):
            if (i==0):
                pass
            #if (i==len(b)):
             #   cnt+=1
              #  d.append(c)
            if (((b[i-1]!=" ")and (b[i]==' '))or i==len(b)-1):
                cnt+=1
                #d.append(c)
                #c=''
            else:
                pass

        print(cnt)