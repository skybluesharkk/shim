a = int(input())
_list = []
print('Gnomes:')
for i in range(a):
    a,b,c = map(int,input().split())
    _list.append(a)
    _list.append(b)
    _list.append(c)
    y = sorted(_list)
    z = list(reversed(y))
    if _list == y:
        print('Ordered')
        _list.clear()
    elif _list == z:
        print('Ordered')
        _list.clear()
    else:
        print('Unordered')
        _list.clear()
