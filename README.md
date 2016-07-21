####obfluentpy3ed
attributes of user-defined functions
```
__annotations__
__call__
__closure__
__code__
__defaults__
__get__
__globals__
__kwdefaults__
__name__
__qualname__
```
If dontwant to support variable positional arguments but still want keyword-only arguments,
```
def f(a,*,b):
    return a,b
f(2,b=1)  #2,1
```
#####cp7
######closures
A closure is a function with an extended scope that encompasses nonglobal variables referenced in the body of the function but not defined there.

######cp9
using repr with tuple
```
def __repr__(self):
    class_name = type(self).__name__
    return '{}({!r}, {!r})'.format(class_name, *self)
```

```
brl = 1/2.43
brl #0.4115226337448559
format(brl, '0.4f') # '0.4115'
'1 BRL = {rate:0.2f} USD'.format(rate=brl) #'1 BRL = 0.41 USD'
```

implement __format__method
```
def __format__(self, fmt_spec=''):
    components = (format(c, fmt_spec) for c in self) #formatted single item
    return '({}, {})'.format(*components)   #format of formats
```
#####cp14
######A Closer Look at the iter Function
using iter() in readlines
```
with open('mydata.txt') as fp:
        for line in iter(fp.readline, '\n'):
            process_line(line)
```
#####cp15
with blocks don’t define a new scope, as functions and modules do.
######cp16
equivalent
```
 def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i
```
```
def gen():
    yield from 'AB'
    yield from range(1, 3)
...
```