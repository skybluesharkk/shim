ans = int(input())
a,b,c,d,e = map(int,input().split())
anss = []
anss.append(a)
anss.append(b)
anss.append(c)
anss.append(d)
anss.append(e)
j=0
for i in range(5):
    if ans == anss[i]:
        j+=1
    else:
        pass
print(j)