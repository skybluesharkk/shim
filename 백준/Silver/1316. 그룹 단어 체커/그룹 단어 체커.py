num = int(input())

#print(num)
cnt=0
for i in range(num):
    word = list(str(input()))
    box = []
    #print(len(word))
    for j in range(len(word)):
        #print(j, word[j])
        if word[j] in box:
            if word[j-1] == word[j]:
                box.append(word[j])
            else:
                cnt+=1
                break
        else:
            box.append(word[j])
        #cnt+=1
    #print(i)
    #print(word)
print(num-cnt)
