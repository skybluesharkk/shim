infi = 10**9

n = int(input())
cnt=0
ans = list(map(int,input().split()))
tmp=0
#print(ans)

t,p=map(int,input().split())

for i in range(len(ans)):
    if ans[i]==0:
        continue
    if ans[i]<=t:
        cnt+=1
    else:
        '''
        tmp=t
        for j in range(infi):
            tmp+=t
            cnt+=1
            if tmp>=ans[i]:
                break
        cnt+=1
        '''
        tmp = ans[i]//t
        tmp2 = ans[i]%t
        if tmp2!=0:
            tmp+=1
        cnt+=tmp

    #print(t,ans[i])
    #print(cnt)
print(cnt)
#print('t',t)
'''
펜은 남거나 부족해서는 안되고 몫 구하기 + 남는 나머지 만큼만 낱개로 구매하기
'''

mx = n//p
#print(mx)
nx = n%p
print(mx,nx)