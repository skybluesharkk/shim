a = list(map(int,input()))
b = list(map(int,input()))
ans=[]
ans.append(int(''.join(map(str,a)))*b[2])
ans.append(int(''.join(map(str,a)))*b[1])
ans.append(int(''.join(map(str,a)))*b[0])
for i in range(len(ans)):
    print(ans[i])
print(int(ans[0]*1+ans[1]*10+ans[2]*100))