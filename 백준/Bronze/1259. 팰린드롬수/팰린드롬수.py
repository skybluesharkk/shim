while(1):
    ans=1
    a = list(map(int,input()))
    if (len(a)==1)and(a[0]==0):
        break
    else:
        b = list(reversed(a))
        for i in range(len(a)):
            if (a[i]!=b[i]):
                ans=0
                break

        if (ans==1):
            print('yes')
        else:
            print('no')