n = int(input())
ans = n
tmp=0
cnt=0
while 1:
    l = n//10
    r = n%10
    s = l+r
    tmp = r*10 + (s%10)
    cnt+=1
    #print('n',n,'tmp',tmp,'r',r,'l',l,cnt)
    if ans == tmp:
        print(cnt)
        break
    else:
        n = tmp
 