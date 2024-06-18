import sys

n,m = map(int,input().strip().split())
n_set = set()
m_set = []
for i in range(n):
    origin = sys.stdin.readline().strip()
    n_set.add(origin)
for j in range(m):
    new = sys.stdin.readline().strip()
    m_set.append(new)
cnt=0
for k in range(len(m_set)):
    if m_set[k] in n_set:
        cnt+=1
print(cnt)