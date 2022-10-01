a=str(input())
alphabet=[0 for x in range(26)]
for i in range(len(a)):
    if a[i] == 'a':
        alphabet[0]+=1
    elif a[i] == 'b':
        alphabet[1]+=1
    elif a[i] == 'c':
        alphabet[2]+=1
    elif a[i] == 'd':
        alphabet[3]+=1
    elif a[i] == 'e':
        alphabet[4]+=1
    elif a[i] == 'f':
        alphabet[5]+=1
    elif a[i] == 'g':
        alphabet[6]+=1
    elif a[i] == 'h':
        alphabet[7]+=1
    elif a[i] == 'i':
        alphabet[8]+=1
    elif a[i] == 'j':
        alphabet[9]+=1
    elif a[i] == 'k':
        alphabet[10]+=1
    elif a[i] == 'l':
        alphabet[11]+=1
    elif a[i] == 'm':
        alphabet[12]+=1
    elif a[i] == 'n':
        alphabet[13]+=1
    elif a[i] == 'o':
        alphabet[14]+=1
    elif a[i] == 'p':
        alphabet[15]+=1
    elif a[i] == 'q':
        alphabet[16]+=1
    elif a[i] == 'r':
        alphabet[17]+=1
    elif a[i] == 's':
        alphabet[18]+=1
    elif a[i] == 't':
        alphabet[19]+=1
    elif a[i] == 'u':
        alphabet[20]+=1
    elif a[i] == 'v':
        alphabet[21]+=1
    elif a[i] == 'w':
        alphabet[22]+=1
    elif a[i] == 'x':
        alphabet[23]+=1
    elif a[i] == 'y':
        alphabet[24]+=1
    elif a[i] == 'z':
        alphabet[25]+=1
    else:
        pass
for j in alphabet:
    print(j,end=' ')