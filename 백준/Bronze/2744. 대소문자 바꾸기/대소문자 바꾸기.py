import sys

n = list(sys.stdin.readline())

for i in range(len(n)):
    if 64 < ord(n[i]) < 91:
        n[i] = n[i].lower()
    elif 96 < ord(n[i]) < 123:
        n[i] = n[i].upper()
    else:
        pass

result = ''.join(s for s in n)
print(result)