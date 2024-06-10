import sys
sets = set()
num = int(input())
# all,empty가 문제네. 무지성으로 넣으면 안되고 두개는 따로 해야 하는데.

for i in range(num):
    ori_order = (sys.stdin.readline().strip())
    if ori_order=='all':
        sets = set(range(1,21))
    elif ori_order=='empty':
        sets.clear()
    else:
        order,x = ori_order.split()
        x = int(x)
        if order == 'add':
            sets.add(x)
        elif order == 'remove':
            sets.discard(x)
        elif order == 'check':
            if x in sets:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if x in sets:
                sets.remove(x)
            else:
                sets.add(x)