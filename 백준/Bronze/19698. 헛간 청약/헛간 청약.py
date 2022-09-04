n,w,h,l = map(int,input().split())
ans = ((w//l)*(h//l))
if n>=ans:
    print(ans)
else:
    print(n)