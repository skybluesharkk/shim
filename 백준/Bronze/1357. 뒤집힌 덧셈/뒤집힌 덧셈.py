def _rev(a):
    _a = list(map(int,str(a)))
    _a.reverse()
    return int(''.join(map(str,_a)))

n1,n2=map(int,input().split())
print(_rev(_rev(n1)+_rev(n2)))