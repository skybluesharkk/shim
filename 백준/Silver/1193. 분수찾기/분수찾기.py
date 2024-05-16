# 특정 수를 입력받으면
# 1부터 더해가면서 그 숫자가 어디까지 커버되는 지 찾는다.
# 생각해보니 for문으로 찾아도 되는 듯 하다.
# 어디까지 커버되는 지 찾으면
# 그 숫자가 어디 칸에 위치하는 지를 찾는다.
# 3 2/1
# 6 1/3
# 10 4/1
# 15 1/5

num = int(input())

i = 1
j=1
bags=[]
x = 0
while i<=num:
    bags.append(j)
    j+=1
    i+=j

k=0
for k in range(len(bags)):
    k+= bags[k]
a = i-j
#print('a',a)

if a==num:
    if len(bags) % 2 == 0:
        # len(bags)+1부터 시작.
        ans = []
        for l in range(bags[-1] ):
            ans.append([ l +1,bags[-1] - l])
        k_n = ans[num - i + j - 1]
        #print(ans)
        #print(k_n)
        pass
    else:
        ans = []
        for l in range(bags[-1] ):
            ans.append([bags[-1]  - l,l + 1])
        k_n = ans[-1]
        #print(ans)
        #print(k_n)
        pass
    #print(ans)
    print(str(k_n[0]) + '/' + str(k_n[1]))
    pass
else:
    if len(bags) % 2 == 0:
        # len(bags)+1부터 시작.
        ans = []
        for l in range(bags[-1] + 1):
            ans.append([bags[-1] + 1 - l, l + 1])
        k_n = ans[num - i + j - 1]
        #print(k_n)
        pass
    else:
        ans = []
        for l in range(bags[-1] + 1):
            ans.append([l + 1, bags[-1] + 1 - l])
        k_n = ans[num - i + j - 1]
        #print(k_n)
        pass
    #print(ans)
    print( str(k_n[0]) + '/' + str(k_n[1]))
    pass
#print(90000000)
#print('i',i)
#print('j',j)
#print('num',num)
#print('bags',bags)
#print('x',x)
#print('k',k)
#print(num-k)




