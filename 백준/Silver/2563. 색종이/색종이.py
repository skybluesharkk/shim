import sys
maps = []

for i in range(100):
    line = []
    for j in range(100):
        line.append(0)
    maps.append(line)

#print(maps)

n = int(input())

for k in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    #a a+10
    #b,b+10
    for l in range(a,a+10):
        for p in range(b,b+10):
            maps[l][p]=1
cnt=0
for i in range(len(maps)):
    for k in range(len(maps[i])):
        if maps[i][k]!=0:
            cnt+=1
print(cnt)