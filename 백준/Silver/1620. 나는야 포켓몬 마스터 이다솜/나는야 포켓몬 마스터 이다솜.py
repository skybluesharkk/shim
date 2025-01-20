import sys

n,m = map(int, input().split())

po, qu = {},[]
for i in range(1,n+1):
    tmp = sys.stdin.readline().strip()
    po[i] = tmp

for j in range(m):
    tmp2 = sys.stdin.readline().strip()
    qu.append(tmp2)

po_r = dict(map(reversed,po.items()))
for k in range(m):
    if qu[k].isdecimal():
        print(po[int(qu[k])])
    else:
       print(po_r[qu[k]])
       pass