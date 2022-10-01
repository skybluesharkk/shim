def ives(a):
    return a**4+a**3+a**2+a+1
while 1:
    a=float(input())
    if a == 0:
        break
    else:
        print("%.2f"%ives(a))