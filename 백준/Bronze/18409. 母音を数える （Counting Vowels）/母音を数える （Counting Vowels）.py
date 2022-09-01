a = ['a','i','u','e','o']
b = int(input())
c = input()
j=0
for i in range(b):
    if c[i] in a:
        j+=1
print(j)