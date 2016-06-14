__author__ = 'Hernan Y.Ke'
import numpy
from time import perf_counter as pc
import array

#floats = numpy.loadtxt('./large.txt') #fails
#print(floats)

floats = array.array('d')
t0=pc()
fp = open('./large.txt','rb')
print(fp)
floats.fromfile(fp,10**2)

print(floats)
print(pc()-t0)