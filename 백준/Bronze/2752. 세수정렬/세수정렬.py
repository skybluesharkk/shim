_num = []
a,b,c = map(int, input().split())
_num.append(a)
_num.append(b)
_num.append(c)
_num.sort()
for i in range(3):
    print(_num[i],end=" ")