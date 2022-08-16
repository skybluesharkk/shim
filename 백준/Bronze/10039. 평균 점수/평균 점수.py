b = []
for i in range(5):
    a = int(input())
    b.append(a)
for i in range(5):
    if b[i]<40:
        b[i]=40
    else:
        pass
print(int(sum(b,0)/len(b)))