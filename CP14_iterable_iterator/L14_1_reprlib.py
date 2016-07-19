__author__ = 'Hernan Y.Ke'
import re
import reprlib
reg = re.compile('\w+')     #put outside of class
class Sentence:

    def __init__(self,sentence):
        self.sentence = sentence
        self.words = reg.findall(sentence)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.sentence) #reprlib.repr generate abbrivated sentence

##test
s = Sentence('test python p')
for word in s:
    print(word)

