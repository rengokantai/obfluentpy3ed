__author__ = 'Hernan Y.Ke'
def make_aver_nonlocal():
    count=0
    total=0
    def averg(new_value):
        nonlocal count,total  # numbers are mutable, If try to redind them, then you are implicitly creating a local variable countm it is no longer a free variable.
        count+=1
        total+=new_value
        return total/count
    return averg

