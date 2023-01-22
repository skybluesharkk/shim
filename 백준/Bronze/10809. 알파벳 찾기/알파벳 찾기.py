s = input()

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ans_a = []

for i in range(26):
    ans_a.append(-1)

for i in range(len(s)):
    for j in range(len(letters)):
        if (s[i]==letters[j]):
            if (ans_a[j]==-1):
                ans_a[j] = i
            else:
                pass

for k  in range(len(ans_a)):
    if (k!=len(ans_a)):
        print(ans_a[k],end=" ")
    else:
        print(ans_a[k])