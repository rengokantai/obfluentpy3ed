__author__ = 'Hernan Y.Ke'
from types import MappingProxyType

d={1:'a'}

d_proxy = MappingProxyType(d)
d[2]='b'
print(d_proxy[2])