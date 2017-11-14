""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""
# Birkac cumle olusturalim.
# let's create some sentences.

sentence_1 = ['I', 'can', 'not', 'believe', 'how', 'hot', 'it', 'is', 'today', '.']
sentence_2 = ['I', 'like', 'going ', 'out ', 'to', 'parties ', 'with ', 'friends', '.']

# cumlelerin uzunlugu, kelime sayisi
print "Length of Sentence 1 :", len(sentence_1)
print "Length of Sentence 2 :", len(sentence_2)

print "-" * 100
# sirali kelimeler
print "Sorted Words (sentence 1) :", sorted(sentence_1)
print "Sorted Words (sentence 2) :", sorted(sentence_2)

print "-" * 100
# iki cumleyi birlestirmek
print "Append Two Sentences : ", sentence_1 + sentence_2

print "-" * 100
# sirali kelimeler
print "Sorted Set of Words : ", sorted(set(sentence_1 + sentence_2))

print "-" * 100
# yeni kelimeler eklemek
sentence_1.append("Hey")
sentence_1.append("!")
print "Append New Words :", ' '.join(sentence_1)

print "-" * 100
# listeyi indekslemek
print "Indexing Lists (sentence_1[0]): ", sentence_1[0]
print "Indexing Lists (sentence_1[1:3]): ", sentence_1[1:3]
print "Indexing Lists (sentence_1[3:-1]): ", sentence_1[3:-2]
print "Indexing Lists (sentence_1[-1]): ", sentence_1[-1]
print "-" * 100
print "Indexing Lists (sentence_1.index('hot')): ", sentence_1.index('hot')
print "Indexing Lists (sentence_1.index('Hey')): ", sentence_1.index('Hey')
