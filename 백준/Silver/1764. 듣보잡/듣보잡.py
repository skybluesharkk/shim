import sys


n,m = map(int, input().split())
nh, ns = [],[]
for i in range(n):
    tmp = sys.stdin.readline().strip()
    nh.append(tmp)

for j in range(m):
    tmp2 = sys.stdin.readline().strip()
    ns.append(tmp2)

nh = set(nh)
ns = set(ns)
a_list = nh&ns
a_list = list(a_list)
a_list.sort()
print(len(a_list))
for k in range(len(a_list)):
    print(a_list[k])