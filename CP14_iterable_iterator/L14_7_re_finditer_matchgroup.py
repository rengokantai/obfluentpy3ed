__author__ = 'Hernan Y.Ke'
import re
import reprlib
reg = re.compile('\w+')     #put outside of class
#lazy impl
class Sentence:

    def __init__(self,sentence):
        self.sentence = sentence

    def __iter__(self):
        for match in reg.finditer(self.sentence):
            yield match.group()

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.sentence) #reprlib.repr generate abbrivated sentence

s = Sentence('test python pu')
for word in s:
    print(word)