__author__ = 'Hernan Y.Ke'
import functools
import time

def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t1=time.time()
        res=func(*args,**kwargs)
        elapsed = time.time()-t1
        name=func.__name__
        arg_lst=[]
        if args:
            arg_lst.append(','.join((repr(arg) for arg in args)))
        if kwargs:
            pairs = ['%s=%r'%(k,w)for k,w in sorted(kwargs.items())]
            arg_lst.append(','.join(pairs))
        arg_str=','.join(arg_lst)
        print('[%0.8fs] %s (%s)->%r' %(elapsed,name,arg_str,res))
        return res
    return clocked

@clock
def snooze(sec):
    time.sleep(sec)

@clock
def fac(n):
    return 1 if n<2 else n*fac(n-1)

if __name__=='__main__':
    print('*'*40,'calling snooze(1)')
    snooze(1)
    print('*'*40,'calling fac(6)')
    print('6!=',fac(6))
