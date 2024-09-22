ans=0

for cnt in range(1,1000000):
    va=list(map(int,str(cnt)))
    ans+=sum(va)

print('The sum of the digits in the numbers\nfrom 1 to one million is',f"{ans+1:,}",'.')
