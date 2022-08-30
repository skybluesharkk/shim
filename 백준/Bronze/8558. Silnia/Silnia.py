def facto():
    a = int(input())
    j = 1
    for i in range(1,a+1):
        j = j *i
    _j = list(map(int,str(j)))
    return _j[-1]

print(facto())