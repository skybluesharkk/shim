num = int(input())
for i in range(num):
    _id,a,b,c = map(int,input().split())
    if a+b+c >=55:
        if (a>=35*(0.3)) and (b>=25*(0.3)) and (c>=40*(0.3)):
            print(_id,a+b+c,"PASS")
        else:
            print(_id,a+b+c,"FAIL")
    else:
        print(_id, a+b+c, "FAIL")