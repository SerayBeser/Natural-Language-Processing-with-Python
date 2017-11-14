""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""
# Birkac cumle olusturalim.
# let's create some sentences.

sentence_1 = ['I', 'can', 'not', 'believe', 'how', 'hot', 'it', 'is', 'today', '.']
sentence_2 = ['I', 'like', 'going ', 'out ', 'to', 'parties ', 'with ', 'friends', '.']

print "len(word) < 5  :   ", [w for w in sentence_1 if len(w) < 5]
print "len(word) <= 5 :   ", [w for w in sentence_1 if len(w) <= 5]
print "len(word) == 5 :   ", [w for w in sentence_1 if len(w) == 5]
print "len(word) != 5 :   ", [w for w in sentence_1 if len(w) != 5]
print "-" * 100
print "startswith ('i')  :   ", sorted([w for w in sentence_1 if w.startswith('i')])
print "endswith ('ieve') :   ", sorted([w for w in sentence_1 if w.endswith('ieve')])
print "in ('ot')         :   ", sorted([w for w in set(sentence_1) if 'ot' in w])
print "islower()         :   ", sorted([item for item in set(sentence_1) if item.islower()])
print "isupper()         :   ", sorted([item for item in set(sentence_1) if item.isupper()])
print "-" * 100
print "len sentence 1: ", [len(w) for w in sentence_1]
print "len sentence 2: ", [len(w) for w in sentence_2]
print "-" * 100
print "upper :", [w.upper() for w in sentence_2]
print "-" * 100
sentences = [sentence_1, sentence_2]
for sentence in sentences:
    for token in sentence:
        if token.islower():
            print token, '--> is a lowercase word'
        elif token.istitle():
            print token, '--> is a titlecase word'
        else:
            print token, '--> is punctuation'
