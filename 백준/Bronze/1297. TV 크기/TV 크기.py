d,h,w=map(int,input().split())

x=((d**2)/(h**2+w**2))**(1/2)

print(int(x*h),int(x*w))