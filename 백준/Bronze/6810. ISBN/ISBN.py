a = int(input())
b = int(input())
c = int(input())
_sum = 0
z = 9780921418
_z = list(map(int,str(z)))
for i in range(0, 10, 2):
    _sum += _z[i] * 1 + _z[i + 1] * 3

print('The 1-3-sum is ',end="");print(_sum+a*1+b*3+c*1)