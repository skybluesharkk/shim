import sys

t = int(sys.stdin.readline())

for i in range(t):
    h,w,n = map(int,input().split())

    cnt=0
    for i in range(w):
        for j in range(h):
            #ans[i][j]=str(j)+str(i)
            #print(i+1,j)
            cnt+=1
            if cnt==n:
                tmp = str(i+1)
                if (i+1)<=9:
                    tmp = '0'+str(i+1)
                print(str(j+1)+tmp)
   # print(ans) 