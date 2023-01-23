import sys
n = int(input())
num = 0
stack = []

for i in range(n):
    a = sys.stdin.readline()
    if (a[1]=='u'):
        order = a[0:4]
        b = list(a)
        b.pop()
        b=list(map(int,(b[5::])))
        b=int(''.join(map(str,b)))
        stack.append(b)
    else:
        order = a[:-1]
        if (order == 'push'):
            pass
        elif (order == 'pop'):
            if (len(stack)!=0):
                print(stack[-1])
                stack.pop()
            else:
                print(-1)
        elif (order == 'size'):
            print(len(stack))
        elif (order == 'empty'):
            if (len(stack)!=0):
                print(0)
            else:
                print(1)
        else:#top
            if (len(stack) != 0):
                print(stack[-1])
            else:
                print(-1)