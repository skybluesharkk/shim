from collections import deque

import sys

n,m = map(int,sys.stdin.readline().strip().split())

#chess = [[0 for _ in range(m)]]*n
#print(chess)


ans=[]
for i in range(n):
    ans.append(list(sys.stdin.readline().strip()))
#print(ans)

def print_nums(n,m,ans):
    print(n,m)
    for j in range(n,n+8):
        for k in range(m,m+8):
            print(ans[j][k],end="")
        print('\n')
    print('\n')
#print_nums(1,1,ans)

def check_nums(n,m,ans):

    chess_type1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
               ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
               ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

    chess_type2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
    cnt1,cnt2=0,0
    for j in range(n,n+8):
        for k in range(m,m+8):
            if ans[j][k]!=chess_type1[j-n][k-m]:
                cnt1+=1
                #print(ans[j][k],chess_type1[j-n][k-m])
        #print('\n')

    for j in range(n,n+8):
        for k in range(m,m+8):
            if ans[j][k]!=chess_type2[j-n][k-m]:
                cnt2+=1
                #print(ans[j][k],chess_type2[j-n][k-m])
        #print('\n')
    return min(cnt1,cnt2)

#print(check_nums(1,1,ans))
new_n = n-7
new_m = m-7

def find_result(new_n,new_m,ans):
    res=[]
    for i in range(new_n):
        for j in range(new_m):
            res.append(check_nums(i,j,ans))
            #print_nums(i,j,ans)
    return res

print(min(find_result(new_n,new_m,ans)))