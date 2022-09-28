while 1:
    a = float(input())
    if a == -1:
        break
    else:
        b=0.167
        print('Objects weighing %.2f'%a,'on Earth will weigh %.2f'%(a*b),'on the moon.')