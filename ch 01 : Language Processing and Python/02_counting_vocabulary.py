""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""

# load our data (texts)
# verilerimizi ice aktaralim

from nltk.book import text2

# we use text2.
# text2'yi kullanacagiz.

# len : Return the number of items of a sequence or collection.
# len : text'in uzunlugunu yani karakter sayisini doner
print "-" * 100
print "Number of Words and Punctuation Symbols(Tokens), (Kelime, Noktalama Sayisi):", len(text2)

# tokens : sequence of str
# tokens : text deki kelimelerin listesi

# set of words (distinct words)
# text deki tum kelimeler
print "-" * 100
print "Set of Words (Kelimeler):", set(text2)

# sorted set of words
# sirali tum kelimeler
print "-" * 100
print "Sorted Set of Words (Sirali Kelimeler):", sorted(set(text2))

print "-" * 100
# Kitapta len(text2) token olmasina ragmen, sadece len(set(text2)) kadar ayri kelime var.
print "Although it has", len(text2), "tokens, this book has only", len(set(text2)), "distinct words, or word types. "

print "-" * 100
print "Specific Word Occurrence (word=disappoint):", text2.count('disappoint')
print "Specific Word Occurrence (word=love):", text2.count('love')
print "Specific Word Occurrence (word=genius):", text2.count('genius')
print "Specific Word Occurrence (word=unpleasant):", text2.count('unpleasant')

#  what percentage of the text is taken up by a specific word
# bir kelimenin tum text icerisinde gecme sikligi
print "-" * 100
print "Percentage of Specific Word (word=love):", 100 * float(text2.count('love')) / float(len(text2))
print "Percentage of Specific Word (word=barbarous):", 100 * float(text2.count('barbarous')) / float(len(text2))
