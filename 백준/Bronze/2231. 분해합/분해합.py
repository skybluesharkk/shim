memo = [0] * 1000001
memo[1] = 2
memo[2] = 4
memo[3] = 6

n = int(input())

def check(num):
    res = []
    for i in str(num):
        res.append(i)
    _sum=0
    for j in range(len(res)):
        _sum+=int(res[j])
    _sum+=num
    return _sum

for i in range(1,n+1):
    memo[i] = check(i)
#print(memo[n])
fin=[]
for k in range(n+1):
    if memo[k] == n:
        fin.append(k)
if len(fin)==0:
    print(0)
else:
    print(min(fin))