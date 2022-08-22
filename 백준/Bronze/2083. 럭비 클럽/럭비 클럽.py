while 1:
    a, b, c = map(str,input().split())
    if (a == '#'):
        break
    elif (int(b)>17) or (int(c)>=80):
        print(a,'Senior')
    else:
        print(a,'Junior')