a = input()

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_A = []
ans_a = []
ans_A = []

for i in range(len(letters)):
    letters_A.append(letters[i].upper())
for i in range(26):
    ans_a.append(0)
for i in range(26):
    ans_A.append(0)
for j in range(len(letters)):
    for k in range(len(a)):
        if (a[k]==letters[j]):
            ans_a[j]+=1
for j in range(len(letters)):
    for k in range(len(a)):
        if (a[k]==letters_A[j]):
            ans_A[j]+=1
for l in range(len(ans_a)):
    ans_a[l]+=ans_A[l]

cnt = ans_a.count(max(ans_a))

if (cnt == 1):
    print(letters_A[ans_a.index(max(ans_a))])
else:
    print('?')