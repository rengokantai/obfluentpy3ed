__author__ = 'Hernan Y.Ke'
from operator import itemgetter,attrgetter,methodcaller
dt=[('New','NY'),('Tok','CA')]

for city in sorted(dt,key=itemgetter(1)):
    print(city)

ccname= itemgetter(1,0)  # change index order
for city in dt:
    print(ccname(city))

#attrgetter
s = 'a b c'
upcase = methodcaller('upper')
print(upcase(s))  #s.upper(), str.upper(s)
hipen = methodcaller('replace',' ','-')
print(hipen(s))
