__author__ = 'Hernan Y.Ke'

"""
found = len(needles & heystack)
"""
# same as
needles={1,2,3}
heystack={1,2,3,4,5}
found = len(needles & heystack)
#found =0
# for i in needles:
#     for j in heystack:
#         if i==j:
#             found+=1
print(found)