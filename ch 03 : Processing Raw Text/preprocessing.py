""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Preprocessing (only words)
 (Manual Cleaning & NLTK cleaning and stemming) ****

"""
from nltk.corpus import gutenberg, stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

import string


def cleaning(text):
    """ CLEANING DATA , veri yi temizleyelim.
    :param text: raw text
    :return: cleaned wordlist
    """
    # 1- Select Only Words, sadece kelimeleri secelim.
    words = str(text).split()

    # 2- Remove Punctuation, noktalama isaretlerini silelim.
    for i in range(0, len(words)):
        for punct in string.punctuation:
            if str(punct) in words[i]:
                words[i] = str(words[i]).replace(str(punct), ' ')

    # 3- Normalizing Case, buyuk kucuk harf normalizasyonunu yapalim.
    words = [w.lower() for w in words]

    # 4- Remove StopWords, stopwords leri kaldiralim.
    stop_words = ['a', 'about', 'above', 'across', 'after', 'afterwards']
    stop_words += ['again', 'against', 'all', 'almost', 'alone', 'along']
    stop_words += ['already', 'also', 'although', 'always', 'am', 'among']
    stop_words += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
    stop_words += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
    stop_words += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
    stop_words += ['because', 'become', 'becomes', 'becoming', 'been']
    stop_words += ['before', 'beforehand', 'behind', 'being', 'below']
    stop_words += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
    stop_words += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
    stop_words += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
    stop_words += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
    stop_words += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
    stop_words += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
    stop_words += ['every', 'everyone', 'everything', 'everywhere', 'except']
    stop_words += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
    stop_words += ['five', 'for', 'former', 'formerly', 'forty', 'found']
    stop_words += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
    stop_words += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
    stop_words += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
    stop_words += ['herself', 'him', 'himself', 'his', 'how', 'however']
    stop_words += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
    stop_words += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
    stop_words += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
    stop_words += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
    stop_words += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
    stop_words += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
    stop_words += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
    stop_words += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
    stop_words += ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
    stop_words += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
    stop_words += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
    stop_words += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
    stop_words += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
    stop_words += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
    stop_words += ['some', 'somehow', 'someone', 'something', 'sometime']
    stop_words += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
    stop_words += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
    stop_words += ['then', 'thence', 'there', 'thereafter', 'thereby']
    stop_words += ['therefore', 'therein', 'thereupon', 'these', 'they']
    stop_words += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
    stop_words += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
    stop_words += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
    stop_words += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
    stop_words += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
    stop_words += ['whatever', 'when', 'whence', 'whenever', 'where']
    stop_words += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
    stop_words += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
    stop_words += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
    stop_words += ['within', 'without', 'would', 'yet', 'you', 'your']
    stop_words += ['yours', 'yourself', 'yourselves']

    words = [w for w in words if w not in stop_words]

    # 5- Remove One-Length Characters, tek karakterli kelimeleri silelim.
    words = [w for w in words if len(w) > 1]

    # 6- Remove Digits, sayilari silelim.
    words = [w for w in words if not w.isdigit()]

    # Now, we have a list of cleaned words.
    # Simdi, temizlenmis kelime listemiz var.
    return words


def cleaning_and_stemming(text, non_alpha=True, normalization=True, stemming=True, stopword=True):
    """ CLEANING DATA , veri yi temizleyelim.
        STEMMING WORDS , kelimelerden kelime kokune gitme islemine stem deniyor.
    :param normalization: default True
    :param non_alpha: default True
    :param stopword: default True
    :param stemming: default True
    :param text: raw text
    :return: cleaned and stemmed wordlist
    """
    # 1- Select Only Words, sadece kelimeleri secelim.
    words = word_tokenize(text)

    # 2- Remove All Non-Alphanumeric Characters , alfabede olmayan tum karakterleri silelim.
    if non_alpha:
        words = [word for word in words if word.isalpha()]

    # 3- Normalizing Case, buyuk kucuk harf normalizasyonunu yapalim.
    if normalization:
        words = [w.lower() for w in words]

    # 4- Remove StopWords, stopwords leri kaldiralim.
    if stopword:
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if w not in stop_words]

    # Now, we have a list of cleaned words.
    # Simdi, temizlenmis kelime listemiz var.
    if stemming:
        porter = PorterStemmer()
        words = [porter.stem(word) for word in words]
    return words


def demo():
    """ LOAD DATA , veri setini yukleyelim.
        """
    # Sense and Sensibility by Jane Austen 1811
    text = gutenberg.raw('austen-sense.txt')
    print "Manual CLeaning : \n", cleaning(text)
    print "\nNLTK: Cleaning & Stemming : \n", cleaning_and_stemming(text)


if __name__ == '__main__':
    demo()
