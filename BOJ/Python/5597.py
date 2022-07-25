stu = []
stu1 = []
stu2 = []

for i in range(28):
    n = int(input())
    stu.append(n)
stu.append(0)
stu.append(0)

for i in range(30):
    stu1.append(i+1)

for i in range(30):
    if stu[i] in stu:
        pass
    else:
        stu2.append(i)
print(stu)
print(stu1)
print(stu2)
