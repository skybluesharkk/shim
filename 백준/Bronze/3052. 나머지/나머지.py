tmp=[]
for i in range(10):
    a = int(input())
    tmp.append(a%42)

cnt=0
tmp2=[]
for k in range(len(tmp)):
    if k==0:
        tmp2.append(tmp[k])
    else:
        if tmp[k] not in tmp2:
            tmp2.append(tmp[k])
print(len(tmp2))