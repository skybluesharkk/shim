a,b = map(int,input().split())

aa = list(map(int,str(a)))
aa.reverse()
bb = list(map(int,str(b)))
bb.reverse()
aaa = aa[0]*100+aa[1]*10+aa[2]
bbb = bb[0]*100+bb[1]*10+bb[2]

print(max(aaa,bbb))