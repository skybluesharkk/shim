import sys
from collections import deque

n = int(sys.stdin.readline().strip())


for i in range(n):
    nums, want = map(int,sys.stdin.readline().split())
    papers = list(map(int,sys.stdin.readline().split()))
    
    printer = deque(papers)
    cnt=0
    
    while printer:
        big = max(printer)
        now = printer.popleft()
        if now == big:
            cnt+=1
            if (want==0):
                print(cnt)
                break
            else:
                want -=1
        else:
            printer.append(now)
            if (want == 0):
                want = len(printer)-1
            else:
                want -=1