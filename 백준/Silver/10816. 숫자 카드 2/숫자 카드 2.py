import sys
from collections import *

sg = int(input())

cards = list(map(int,sys.stdin.readline().split()))
ncd = Counter(cards)
#for i in range(len(cards)):
 #   ncd[cards[i]] = cards.count(cards[i])

ncd_keys = ncd.keys()

m = int(input())

tmp = list(map(int,sys.stdin.readline().split()))

for i in range(len(tmp)):
    if tmp[i] not in ncd_keys:
        tmp[i]=0
    else:
        tmp[i]=ncd[tmp[i]]

for k in range(len(tmp)-1):
    print(tmp[k],end=" ")
print(tmp[-1])