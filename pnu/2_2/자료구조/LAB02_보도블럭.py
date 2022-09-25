hl = list(map(int, input().split()))
hr = list(map(int, input().split()))
hl.remove(-9)
hr.remove(-9)

block = [[0 for x in range(max(hl))] for y in range(len(hl))]

for p in range(0,len(block)):
    for j in range(len(hl)):
        for l in range(hl[j]):
            block[j][l]=1

for p in range(0,len(block)):
    for j in range(len(hr)):
        if hr[j]==-1:
            pass
        elif hr[j]==0:
            pass
        else:
            for l in range(hr[j],0,-1):
                block[j][max(hl)-l]=1

vt=[]
vb=[]
nvt=0
nbt=0

for x in range(max(hl)):
    nvt=0
    for y in range(len(block)):
        if block[y][x]==1:
            nvt+=1
        elif block[y][x]==0:
            break
        else:
            pass
    vt.append(nvt)


for x in range(max(hl)):
    nvb=0
    for y in range(len(block)-1,0,-1):
        if block[y][x]==1:
            nvb+=1
        elif block[y][x]==0:
            break
        else:
            pass
    vb.append(nvb)

for nbb in range(len(vb)):
    if vb[nbb]==len(block)-1:
        vb[nbb] = -1
    else:
        pass

print(*vt,'-9')
print(*vb,'-9')

for i in range(len(block)):
    for j in range(len(block[i])):
        print(block[i][j], end=' ')
    print()
