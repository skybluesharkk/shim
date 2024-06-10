import sys

# 초기화
sets = set()
num = int(input())

for _ in range(num):
    ori_order = sys.stdin.readline().strip()

    if ori_order == 'all':
        sets = set(range(1, 21))
    elif ori_order == 'empty':
        sets.clear()
    else:
        order, x = ori_order.split()
        x = int(x)

        if order == 'add':
            sets.add(x)
        elif order == 'remove':
            sets.discard(x)  # discard는 존재하지 않아도 에러가 발생하지 않음
        elif order == 'check':
            print(1 if x in sets else 0)
        elif order == 'toggle':
            if x in sets:
                sets.remove(x)
            else:
                sets.add(x)
