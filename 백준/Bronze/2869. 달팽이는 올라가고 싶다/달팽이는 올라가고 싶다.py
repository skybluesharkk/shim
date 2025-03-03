import sys

a,b,v = map(int,sys.stdin.readline().strip().split())
distance = 0

k = (v-b)/(a-b)

print(int(k) if k == int(k) else int(k)+1)