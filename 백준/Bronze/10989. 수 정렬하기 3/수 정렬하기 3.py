import sys

n = int(sys.stdin.readline().strip())


#print(ans)

def count_sort(n):
    cnt = [0] * (10000 +1)
    for _ in range(n):
        cnt[int(sys.stdin.readline().strip())] +=1
    
   
    for i in range(len(cnt)):
        if cnt[i]!=0:
            for _ in range(cnt[i]):
                print(i)

count_sort(n)