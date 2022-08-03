while 1:
    try:
        a, b = map(int, input().split())
        if (a == 0) and (b == 0):
            break
        elif a > b:
            print('Yes')
        else:
            print('No')
    except EOFError:
        break