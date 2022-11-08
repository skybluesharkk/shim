n = int(input())
Old=[]
Adult=[]
Child=[]

for i in range(n):
    tmp = list(map(str,input().split()))

    if tmp[2]=='M':
        tmp[2]=0
    else:
        tmp[2]=1
    tmp[0]=int(tmp[0])
    tmp[1]=int(tmp[1])
    if tmp[1]<=15:
        Child.append(tmp)
    elif tmp[1]>=16 and tmp[1]<=60:
        Adult.append(tmp)
    else:
        Old.append(tmp)


Old = sorted(Old, key=lambda x:x[2])

for i in range(len(Adult)):
    if Adult[i][2] == 1:
        Adult[i][2] =0
    else:
        Adult[i][2]=1
Adult = sorted(Adult,key=lambda x:x[2])

for i in range(len(Old)):
    print(Old[i][0])
for i in range(len(Child)):
    print(Child[i][0])
for i in range(len(Adult)):
    print(Adult[i][0])
