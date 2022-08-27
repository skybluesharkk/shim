q = [ 'a', 'e', 'i', 'o', 'u','A','E','I','O','U']

while 1:
    a = input()
    if (a == '#'):
        break
    j = 0
    for i in range(len(a)):
        if a[i] in q:
            j+=1
    print(j)