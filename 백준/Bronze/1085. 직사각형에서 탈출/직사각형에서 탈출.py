x,y,w,h = map(int,input().split())

a =[x,y]
a.append(w-x)
a.append(h-y)
print(min(a))