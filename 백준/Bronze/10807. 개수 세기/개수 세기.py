import sys
a = int(input())
b = list(map(int, sys.stdin.readline().split()))
c = int(input())
j=[]

for i in range(a):
    if c == b[i]:
        j.append(c)
    else:
        pass

print(len(j))
