a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

sci = []
mun = []

sci.append(a)
sci.append(b)
sci.append(c)
sci.append(d)
mun.append(e)
mun.append(f)
sci.sort()
mun.sort()
print(sci[-1]+sci[-2]+sci[-3]+mun[-1])