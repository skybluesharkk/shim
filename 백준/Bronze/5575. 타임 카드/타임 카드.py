for i in range(3):
    a = [int(x) for x in input().strip().split()]
    b = a[3]*3600+a[4]*60+a[5] - a[0]*3600-a[1]*60-a[2]
    print(b//3600,(b%3600)//60,((b%3600)%60)%60)