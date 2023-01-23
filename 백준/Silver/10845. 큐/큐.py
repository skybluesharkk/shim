import sys
n = int(input())
num = 0
queue = []

for i in range(n):
    a = sys.stdin.readline()
    if (a[1]=='u'):
        order = a[0:4]
        b = list(a)
        b.pop()
        b=list(map(int,(b[5::])))
        b=int(''.join(map(str,b)))
        queue.append(b)
    else:
        order = a[:-1]
        if (order == 'push'):
            pass
        elif (order == 'pop'):
            if (len(queue)!=0):
                print(queue[0])
                queue.pop(0)
            else:
                print(-1)
        elif (order == 'size'):
            print(len(queue))
        elif (order == 'empty'):
            if (len(queue)!=0):
                print(0)
            else:
                print(1)
        elif (order == 'front'):
            if (len(queue)!=0):
                print(queue[0])
            else:
                print(-1)
        else:#top
            if (len(queue) != 0):
                print(queue[-1])
            else:
                print(-1)