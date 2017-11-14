""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch02.html

Python ile Dogal Dil Isleme

"""

"""
A lexicon, or lexical resource, is a collection of words and/or phrases along with associated
information, such as part-of-speech and sense definitions.

Sozcuksel veya sozlu kaynak, sozcuk veya cumlelerin yani sira konusma ve anlam
tanimlarinin bir parcasi gibi iliskili bilgilerden olusan bir derlemedir. 
"""

import nltk


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)


def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return float(len(content)) / float(len(text))


# kullanilmayan sozcukler
print "Unusual Words    :", unusual_words(nltk.corpus.inaugural.words('1789-Washington.txt'))
print "-" * 100
# stopwordsler ( a, an, the, my, you, ...)
print "Stopwords        :", nltk.corpus.stopwords.words('english')
print "-" * 100
# stopwordler textten cikartildiginda geriye kalan kelimeler text'in kacta kacini olusturuyor
# print "Content Fraction :", content_fraction(nltk.corpus.reuters.words())

"""
A Word Puzzle: a grid of randomly chosen letters with rules for creating words
out of the letters; this puzzle is known as "Target."

Bir Kelime Bulmacasi: harflerden kelimeleri olusturmak icin kurallarla rastgele secilen harflerden
olusan bir tablo; bu bulmaca "Hedef" olarak bilinir.

"""

puzzle_letters = nltk.FreqDist('seraybhn')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
print [w for w in wordlist if len(w) >= 6
       and obligatory in w
       and nltk.FreqDist(w) <= puzzle_letters]

