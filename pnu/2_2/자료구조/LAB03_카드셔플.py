def cardshuffle(list):
    n = len(list)
    _result = []
    if n%2==0:
        n2 = int(n)/2
        l1 = list[0:int(n2)]
        l2 = list[int(n2):n]
        for i in range(int(n2)):
            _result.append(l1[i])
            _result.append(l2[i])
    else:
        n2 = int(n//2)
        l1 = list[0:n2+1]
        l2 = list[n2+1:n]
        for i in range(int(n2)):
            _result.append(l1[i])
            _result.append(l2[i])
        _result.append(l1[n2])
    return _result

def allshuffle(list):
    sa = []
    tmp = []
    tmp.extend(list)
    for i in list:
        sa.append(cardshuffle(tmp))
        tmp = cardshuffle(tmp)
    return sa
def allshufflecut(list):
    allshuffle(list)
    for k in allshuffle(list):
         if k ==list[0]:
             cutlist=list[0:k]
             break
         else:
             pass
    return cutlist
def find1to2(list1,list2):
    n = 0
    for i in allshuffle(list1):
        if i == list2:
            n += 1
            break
        n += 1
    return n
a=[]
b=[]
while -9 not in a:
    llist = list(map(int,input().split()))
    a.extend(llist)
while -9 not in b:
    llist2 = list(map(int,input().split()))
    b.extend(llist2)

a.remove(-9)
b.remove(-9)
c = sorted(a)

if a in allshuffle(c) and b in allshuffle(c):
    print(min(find1to2(a,b),find1to2(c,a),find1to2(b,a)))
elif a not in allshuffle(c):
    print('NOT')
elif b not in allshuffle(c):
    print('NOT')
else:
    pass
