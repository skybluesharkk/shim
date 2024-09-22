print('Enter coefficient of restitution: ',end="")
per = str(input())
per = float(per[0::])
print('Enter initial height in meters: ',end="")
mt = int(input())
print('Number of bounces: ',end="")
nm = int(input())

ans=0
while(mt>=0.1):
    ans+=mt
    mt*=per
    ans+=mt

print('Meters traveled: ',round(ans-mt,2))
