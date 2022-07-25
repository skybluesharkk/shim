stu = []
stu1 = []
stu2 = []

for i in range(28):
    n = int(input())
    stu.append(n)
for i in range(30):
    stu1.append(i+1)
for i in stu1:
    if i not in stu:
        stu2.append(i)
stu2.sort()
print(stu2[0])
print(stu2[1])
