n,k = map(int,input().split())

wallet=[]
for i in range(n):
    m = int(input())
    wallet.append(m)
for j in range(n):
    if wallet[j]>k:
        wallet[j]=0
wallet.sort()
wallet.reverse()
#print(wallet)
p=0
num = wallet.count(0)
for i in range(num):
    wallet.remove(0)
for i in range(len(wallet)):
    #print(wallet[i])
    #print(k//wallet[i])
    tmp = k//wallet[i]
    if tmp!=0:
        p+=(tmp)
        k=k%wallet[i]
    else:
        pass
print(p)