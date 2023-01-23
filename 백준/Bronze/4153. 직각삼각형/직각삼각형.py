while (1):
    a,b,c = map(int,input().split())
    if (a==0):
        break
    else:
        d = []
        d.append(a)
        d.append(b)
        d.append(c)
        d.sort()
        if (d[-1]**2==(d[0]**2)+(d[1]**2)):
            print('right')
        else:
            print('wrong')