import sys

x = int(input())
company = []
for i in range(x):
    name, record = map(str,sys.stdin.readline().strip().split())
    if record == 'enter':
        company.append(name)
    if record == 'leave':
        company.remove(name)
#print(company)
company.sort()
#print(company)
for j in range(len(company)-1,-1,-1):
    print(company[j])