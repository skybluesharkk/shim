h,m = map(int,input().split())

if (h==0)and(m!=0):
    h=24
elif (h==0)and(m==0):
    h=23
    m=60
else:
    pass
totaltime = h*60+m

totaltime-=45
if ((int(totaltime/60))!=24):
    print(int(totaltime/60),totaltime%60)
else:
    print(0, totaltime % 60)