n = int(input())
train = [0]
hwamul = [0]

for i in range(n):
    a = int(input())
    hwamul.append(a)
idealhwamul = sorted(hwamul)
howmuchhwamul = len(hwamul)
hwamul.append(0)
lot=None

for i in range(howmuchhwamul):
    if i == 0:
        lot = hwamul[i]
    else:
        if lot == None:
            if hwamul[i]>hwamul[i+1]:
                if hwamul[i]>train[0]:
                    if hwamul[i+1]>train[0]:
                        lot = hwamul[i]
                    else:
                        if hwamul[i+1]>train[-1]:
                            train.insert(0,hwamul[i])
                            break
                        else:
                            lot=hwamul[i]
                else:
                    if hwamul[i]<train[-1]:
                        if hwamul[i+1]>train[-1]:
                            train.append(hwamul[i])
                            hwamul[i]=0
                            break
                        else:
                            lot = hwamul[i]
                            hwamul[i]=0
            if hwamul[i]<hwamul[i+1]:
                if hwamul[i]>train[0]:
                    train.insert(0,hwamul[i])
                else:
                    break
        elif lot != None:
            if lot > hwamul[i] > train[0]:
                train.insert(0,hwamul[i])
                hwamul[i]=0
            elif hwamul[i]>train[0] and hwamul[i] > lot:
                train.insert(0,lot)
                lot = hwamul[i]
                hwamul[i]=0
            elif hwamul[i]<train[-1] and hwamul[i]<lot:
                train.append(lot)
                lot=hwamul[i]
                hwamul[i]=0
            elif hwamul[i]<train[-1] and hwamul[i]>lot:
                train.append(hwamul[i])
                hwamul[i]=0

print(len(train)-1)