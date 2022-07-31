import sys

a = int(input())

for i in range(1,a+1):
    b, c = map(int, sys.stdin.readline().rstrip().split())
    print(b+c)