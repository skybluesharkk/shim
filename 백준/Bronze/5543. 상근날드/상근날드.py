_bur=[]
_dri=[]
_set=[]

for i in range(3):
    a = int(input())
    _bur.append(a)
for i in range(2):
    b = int(input())
    _dri.append(b)
for i in range(3):
    c = _bur[i]+_dri[0] - 50
    d = _bur[i]+_dri[1] - 50
    _set.append(c)
    _set.append(d)
_set.sort()

print(_set[0])