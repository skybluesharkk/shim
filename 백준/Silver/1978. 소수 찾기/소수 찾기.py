
n = int(input())
cnt=0

_input = list(map(int, input().split()))


ans=[]
def isprimenumber(a):
    if (a==1):
        return False
    if (a==2):
        return True
    for i in range(2,a):
        if (a%i==0):
            return False
    return True

for j in range(n):
    if (isprimenumber(int(_input[j]))):
        cnt+=1
        #ans.append(_input[j])
print(cnt)
