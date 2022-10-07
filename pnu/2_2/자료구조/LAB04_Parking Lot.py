def howmuch0in_lot(list):
    count=0
    for i in range(len(list)):
        if list[i]==0:
            count+=1
    return count

lot,number = map(int,input().split())
car = []
_lot = [0 for x in range(lot)]

for i in range(number):
    a = int(input())
    car.append(a)

for i in range(number):
    if (car[i] < 0) and ((-1)*(int(car[i])) not in car[0:i]):
        car[i]=0
    else:
        pass

while 0 in car:
    car.remove(0)

for j in range(len(car)):
    if car[j] > 0:
        if 0 in _lot:
            _lot[_lot.index(0)] = car[j]
        else:
            tmp = len(_lot)
            _lot.extend([0 for x in range(len(_lot))])
            _lot[tmp] = car[j]
    if car[j] < 0:
        _lot[_lot.index((-1)*(int(car[j])))] = 0
        if (howmuch0in_lot(_lot) >= (2/3)*len(_lot)) and int(len(_lot)) > lot:
            tmp = [0 for x in range(int(len(_lot)/2))]
            while 0 in _lot:
                _lot.remove(0)
            for j in range(len(_lot)):
                tmp[j] = _lot[j]
            _lot = tmp

for k in range(len(_lot)):
    if _lot[k] !=0:
        print(k+1,_lot[k])
