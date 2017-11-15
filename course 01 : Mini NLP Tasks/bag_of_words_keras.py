""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Bag Of Words ****

Bag of Words (BoW) is a model used in natural language processing.
One aim of BoW is to categorize documents.
The idea is to analyse and classify different "bags of words" (corpus).
And by matching the different categories, we identify which "bag" a certain block of text (test data) comes from.
https://ongspxm.github.io/blog/2014/12/bag-of-words-natural-language-processing/

Building a "Bag of Words" involves 3 steps:
Kelime Cantasi olusturma 3 asamalidir:

--tokenizing
--counting
--normalizing

Kelime Cantasi- (Bag of Words) (BoW), dogal dil islemesinde kullanilan bir modeldir.
BoW'un bir amaci, belgeleri kategorize etmektir. Amac farkli "canta sozcukleri" 'ni (korpus)
analiz etmek ve siniflandirmaktir. Farkli kategorilere eslestirerek,
belirli bir metin blogunun (test verisi) "cantasini" tanimlamis oluyoruz.
"""
from keras.preprocessing.text import Tokenizer


def bag_of_words_with_keras(texts):
    """

    :param texts: list of sentences
    :return: bag of words (type: numpy matrix)
    """
    t = Tokenizer()
    t.fit_on_texts(texts)
    bows = t.texts_to_matrix(texts, mode='count')
    return bows


def demo():
    text_1 = "John likes to watch movies. Mary likes movies too."
    text_2 = "John also likes to watch football games."
    text_3 = "The quick brown fox jumps over the lazy dog."
    text_4 = "Never jump over the lazy dog quickly."
    print "Keras Bag Of Words :\n", bag_of_words_with_keras([text_1, text_2, text_3, text_4])


if __name__ == '__main__':
    # bag_of_words_with_keras(texts)
    demo()
