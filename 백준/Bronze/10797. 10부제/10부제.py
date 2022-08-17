a = (int(input()))%10
b = [int(x) for x in input().strip().split()]
i = []
for j in range(5):
    if a == b[j]:
        i.append(a)
    else:
        pass
print(len(i))