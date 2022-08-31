a,b,c = map(int,(input().split()))

univ= []
univ.append(a)
univ.append(b)
univ.append(c)
univ2=sorted(univ)
if a+b+c>=100:
    print('OK')
elif univ2[0]==a:
    print('Soongsil')
elif univ2[0]==b:
    print('Korea')
else:
    print('Hanyang')