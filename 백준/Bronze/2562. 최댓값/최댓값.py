tmp = []
b = []
for i in range(9):
    a = int(input())
    tmp.append(a)
b = sorted(tmp)

print(b[-1])
print(tmp.index(b[-1])+1)