""" @SerayBeser

Natural Language Processing with Python
# http://www.nltk.org/book/ch02.html

Python ile Dogal Dil Isleme

"""

"""

# a text corpus is a large body of text.
# Bir metin corpus metnin buyuk bir bolumudur.
# corpora = corpus(plural)(cogulu)

NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus files in a variety of formats.  These
functions can be used to read both the corpus files that are
distributed in the NLTK corpus package, and corpus files that are part
of external corpora.
 
NLTK corpus okuyuculari. Bu paketteki moduller, cesitli bicimlerde 
corpus dosyalarini okumak icin kullanilabilen islevleri saglar. 
Bu islevler, hem NLTK corpus paketinde dagitilan corpus dosyalarini 
hem de dis corpora'nin bir parcasi olan corpus dosyalarini okumak icin kullanilabilir.

Common Structures for Text Corpora: The simplest kind of corpus is a collection of 
isolated texts with no particular organization; some corpora are structured 
into categories like genre (Brown Corpus); some categorizations overlap, such as
topic categories (Reuters Corpus); other corpora represent language use over
time (Inaugural Address Corpus).
 
1- Gutenberg Corpus
2- Web and Chat Text
3- Brown Corpus
4- Reuters Corpus
5- Inaugural Address Corpus
6- Annotated Text Corpora
"""

from nltk.corpus import gutenberg, webtext, brown, reuters, inaugural

print "Gutenberg FileIds   :", gutenberg.fileids()
print "Webtext FileIds     :", webtext.fileids()
print "Brown FileIds       :", brown.fileids()
print "Brown Categories    :", brown.categories()
print "Reuters FileIds     :", reuters.fileids()
print "Reuters Categories  :", reuters.categories()
print "Inaugural FileIds   :", inaugural.fileids()
