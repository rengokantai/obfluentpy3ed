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
