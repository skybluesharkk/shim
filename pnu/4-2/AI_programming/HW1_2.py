import math
print('Enter future value: ',end="")
fv = int(input())
print('Enter interest rate (as %): ',end="")
ir = int(input())
print('Enter number of years:',end="")
n = int(input())
pv = float(fv/(1+ir/100)**n)
print('Present Value: $',f"{round(pv,2):,}")
