sentence = list(str(input()))

#print(sentence)
# 일차적으로 거름망을 먼저 만든 후에
# 이차적으로 거름망을 정렬하면서 단어수를 세야겠다

# 거름망

for i in range(len(sentence)):
    if sentence[i]=='-':
        if sentence[i-1] in ['c','d'] :
            pass
        else:
            sentence[i]=0
    elif sentence[i]=='=':
        if sentence[i-1] in ['c','s','z']:
            pass
        else:
            sentence[i]=0
#print(sentence)
while 0 in sentence:
    sentence.remove(0)
#print(sentence)

cnt = len(sentence)

for j in range(len(sentence)):
    if sentence[j]=='=':
        if sentence[j-1]=='c':
            cnt-=1
        elif sentence[j-1]=='s':
            cnt-=1
        elif sentence[j-1]=='z':
            if sentence[j-2]=='d':
                cnt-=2
            else:
                cnt-=1
    elif sentence[j]=='-':
        if sentence[j-1]=='c':
            cnt-=1
        elif sentence[j-1]=='d':
            cnt-=1
    elif sentence[j]=='j':
        if sentence[j-1]=='l':
            cnt-=1
        elif sentence[j-1]=='n':
            cnt-=1

#print(sentence)
print(cnt)

