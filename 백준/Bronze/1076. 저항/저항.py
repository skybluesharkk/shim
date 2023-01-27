first = str(input())
second = str(input())
third = str(input())
ans=[]
value = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
value_m = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
sum=0
for i in range(len(value)):
    if (first == value[i]):
        sum+=i*10
for i in range(len(value)):
    if (second == value[i]):
        sum+=i*1
for i in range(len(value_m)):
    if (third == value_m[i]):
        sum*=10**i
print(sum)