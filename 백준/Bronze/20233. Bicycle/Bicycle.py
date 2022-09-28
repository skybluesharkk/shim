a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
a1=a+(t-30)*21*x
b1=b+(t-45)*21*y
if a1<=0 and b1<=0:
    print(a,b)
elif a1<=0 and b1>=0:
    print(a,b1)
elif a1>=0 and b1<=0:
    print(a1,b)
else:
    print(a1,b1)
