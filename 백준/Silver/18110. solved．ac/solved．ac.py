import sys
from decimal import Decimal,ROUND_HALF_UP

n = int(sys.stdin.readline().strip())


def custom_decimal(total):
    if total - int(total) >=0.5:
        return (int(total)+1)
    else:
        return int(total)
    
if n==0:
    print(0)
else:
    rs = []
    for i in range(n):
        rs.append(int(sys.stdin.readline().strip()))
    #print(rs)
    rs.sort()
    up = custom_decimal(n*0.15)
    down = custom_decimal(n*0.15)
    #print(up)
    total = 0
    for j in range(down,len(rs)-down):
        total+=rs[j]
    #print(total)
    #print(total/(n-up-down))
    total /= (n-up-down)
    print(custom_decimal(total))
    #print(round(total/(n-up-down)))