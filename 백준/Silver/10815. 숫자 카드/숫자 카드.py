import sys

n = int(sys.stdin.readline().strip())

have_num = set(list(map(int,sys.stdin.readline().strip().split())))

m = int(sys.stdin.readline().strip())

dont_know_num = list(map(int,sys.stdin.readline().strip().split()))

#print(n)
#print(have_num)
#print(m)
#print(dont_know_num)
#ans = []
for i in range(len(dont_know_num)):
    if dont_know_num[i] in have_num:
        #ans.append(1)
        dont_know_num[i]=1
    else:
        #ans.append(0)
        dont_know_num[i]=0
#print(ans)

for j in range(len(dont_know_num)-1):
    print(dont_know_num[j],end=" ")
print(dont_know_num[-1])