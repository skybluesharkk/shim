import sys
n = int(input())

ans = []

for i in range(n):
    #order = sys.stdin.readline()
    order = list(map(str,sys.stdin.readline().split()))
    #print(order)

    if (order[0]=='push_back'):
        ans.append(int(order[1]))
    elif (order[0]=='push_front'):
        ans.insert(0,int(order[1]))
    elif (order[0]=='pop_front'):
        if (len(ans)==0):
            print(-1)
        else:
            print(ans[0])
            ans.remove(ans[0])
    elif (order[0]=='pop_back'):
        if (len(ans)==0):
            print(-1)
        else:
            print(ans[-1])
            ans.pop()
    elif (order[0]=='size'):
        print(len(ans))
    elif (order[0]=='empty'):
        if (len(ans)==0):
            print(1)
        else:
            print(0)
    elif (order[0]=='front'):
        if (len(ans)==0):
            print(-1)
        else:
            print(ans[0])
    elif (order[0]=='back'):
        if (len(ans)==0):
            print(-1)
        else:
            print(ans[-1])
    else:
        pass
    #print(ans)
