""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch01.html

Python ile Dogal Dil Isleme

"""

# load our data (texts)
# verilerimizi ice aktaralim

from nltk.book import *

# we use text2.
# text2'yi kullanacagiz.

print "-" * 100
print "Book (Kitap) : ", text2.name

# Print a concordance for ``word`` with the specified context window.
# Word matching is not case-sensitive.

# With concordance we can look at the words in the text.
# concordance ile text icerisinde gecen kelimelere bakabiliriz.
print "-" * 100
print text2.concordance('love')

# Distributional similarity: find other words which appear in the
# same contexts as the specified word; list most similar words first.

# Dagilim benzerligi: Belirtilen kelime ile ayni baglamlarda gorunen
# diger sozcukleri bulur; sonra en benzer kelimeleri listeleler.
print "-" * 100
print text2.similar('affection')

# Find contexts where the specified words appear; list
# most frequent common contexts first.

# Belirtilen kelimelerin gorundugu baglamlari bulur;
# sonra en sik karsilasilan baglamlari listeler.
print "-" * 100
print text2.common_contexts(['monstrous', 'very'])

# Produce a plot showing the distribution of the words through the text. Requires pylab to be installed.

# Kelimelerin metin boyunca dagilimini gosteren bir grafik olusturur.
text2.dispersion_plot(['love', 'affect', 'sense', 'honour'])


