n , k = map(int,input().split())

ans = []
people = [i for i in range(1,n+1)]
num=0
strp="<"


while people:
    num+=k-1
    if num>=len(people):
        num= num%len(people)
    tmp = people.pop(num)
    ans.append(tmp)

for j in range(len(ans)):
    if j==0:
        strp+=str(ans[j])
    else:
        strp+=", "+str(ans[j])
print(strp+">")