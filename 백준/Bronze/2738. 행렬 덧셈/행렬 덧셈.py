n,m = map(int,input().split())
A = []
B = []
C=[[]]
for i in range(n):
    a = list(map(int,input().split()))
    A.append(a)
for j in range(n):
    b = list(map(int,input().split()))
    B.append(b)

for k in range(n):
    for l in range(m):
        A[k][l]+=B[k][l]

for q in range(len(A)):
    for d in range(len(A[q])):
        if (d!=len(A[q])-1):
            print(A[q][d],end=" ")
        else:
            print(A[q][d])