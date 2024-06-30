import sys
n = int(sys.stdin.readline().strip())
first = sys.stdin.readline().strip().split()
ori_set=set()
for i in range(n):
    ori_set.add(first[i])
m = int(sys.stdin.readline().strip())
second = sys.stdin.readline().strip().split()

for j in range(m):
    if second[j] in ori_set:
        print(1)
    else:
        print(0)