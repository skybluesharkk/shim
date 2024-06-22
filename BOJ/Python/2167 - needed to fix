import sys
n,m = map(int,input().split())
mat = []
for i in range(n):
    nums = sys.stdin.readline().strip().split()
    mat.append(nums)
#print(mat)
k = int(sys.stdin.readline().strip())

prob = []

for j in range(k):
    i,j,x,y = map(int,input().split())
    #print(i,j,x,y)
    prob.append([i,j,x,y])
#print(prob)
total=0
#i,j,x,y
# 2중 for문을 만들어야 하는 데 
'''
쭉 더하다가 중간에 멈춰야 함

(1,1) - (2,3)
-> (0,0) - (1,2)까지를 다 더해야 함

[[1,2,4],[8,16,32]]
(0,2) - (1,2)

'''
def plus(mat,i,j,x,y):
    total=0
    flag = j-1
    for a in range(i-1,len(mat)):
        if a != (i-1):
            flag = 0
        for b in range(flag,len(mat[a])):
           # print(flag)
            total+=int(mat[a][b])
            #print(mat[a][b],total)
            if a==(x-1) and b==(y-1):
               # print(a,b,mat[a][b],total)
                print(total)
                total=0
                break
    
for c in range(len(prob)):
    i,j,x,y = prob[c][0],prob[c][1],prob[c][2],prob[c][3]
    plus(mat,i,j,x,y)

'''


'''
