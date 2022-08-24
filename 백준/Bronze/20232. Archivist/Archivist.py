a = int(input())
cham = [1995,1998,1999,2001,2002,2003,2004,2005,2009,2010,2011,2012,2014,2015,2016,2017,2019]
if (a in cham):
    print('ITMO')
elif (a==2006):
    print('PetrSU, ITMO')
else:
    print('SPbSU')