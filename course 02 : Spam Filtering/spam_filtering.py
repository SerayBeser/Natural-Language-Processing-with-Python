""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Spam Filtering
     Spam Filtreleme ****

dataset : http://www2.aueb.gr/users/ion/data/enron-spam/ : Enron 1
"""
# encoding=utf8
import sys

import warnings
import numpy as np
import collections

from glob import iglob
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from keras.preprocessing.text import Tokenizer

reload(sys)
sys.setdefaultencoding('utf8')
warnings.filterwarnings('ignore')
stop_words = set(stopwords.words('english'))


def cleaning(text):
    """ cleaning and normalizing data , veri yi temizleme ve normalize etme.
    :param text: raw text
    :return: cleaned and normalized wordlist
    """

    words = [word for word in word_tokenize(str(text)) if word.isalpha()]
    return [w.lower() for w in words]


class Bag_of_Words:
    def __init__(self):
        self.corpus = list()
        self.labels = list()
        self.indexes = list()
        self.vocabulary = collections.OrderedDict()

    def create_vocabulary(self, texts):
        """ Updates internal vocabulary based on a list of texts.

        :param texts:
        """
        print "Creating Vocabulary ...",
        self.corpus = cleaning(str(' '.join(texts)).lower())
        self.labels = sorted(set(self.corpus))
        self.indexes = range(0, len(self.labels))
        self.vocabulary = collections.OrderedDict(sorted(dict(zip(self.labels, self.indexes)).items()))
        print "DONE"

    def bag_of_words(self, texts, mode='count'):
        """ Convert a list of texts to a Numpy matrix.

        :param mode:  one of 'binary', 'count', 'freq', default : 'count'
        :param texts: list of sentences
        :return: bag of words (type: numpy ndarray)
        """
        print "Creating Bag of Words ...",
        bows = list()
        count = 0

        for text in texts:
            bow = list()
            text = cleaning(text.lower())
            for v in self.vocabulary:
                if str(mode) == 'count':
                    for t in text:
                        if str(t) == str(v):
                            count += 1
                    bow.append(count)
                    count = 0
                if str(mode) == 'binary':
                    if str(v) in text:
                        bow.append(1)
                    else:
                        bow.append(0)
                if str(mode) == 'freq':
                    for t in text:
                        if str(t) == str(v):
                            count += 1
                    bow.append(count / float(len(text)))
                    count = 0
            bows.append(bow)
        print "DONE"
        return np.asanyarray(bows)


def load_dataset():
    """ Load Enron 1 email dataset

    :return: ham_name, ham_mail, spam_name, spam_mail
    """
    print "Loading Data ...",
    ham_name = list()
    ham_mail = list()
    for f_path in iglob("input/enron1/ham" + '**/*'):
        with open(f_path, 'r') as f:
            ham_name.append(str(f_path).split('/')[-1])
            ham_mail.append((' '.join(f.readlines())).decode('iso-8859-1').encode('utf-8'))

    spam_name = list()
    spam_mail = list()
    for f_path in iglob("input/enron1/spam" + '**/*'):
        with open(f_path, 'r') as f:
            spam_name.append(str(f_path).split('/')[-1])
            spam_mail.append((' '.join(f.readlines())).decode('iso-8859-1').encode('utf-8'))
    print "DONE"
    return ham_name, ham_mail, spam_name, spam_mail


def split(bows_ham, bows_spam):
    """
    default split ratio = 20 / 100
    :param bows_ham:
    :param bows_spam:
    :return:  X_train, X_test, y_train, y_test
    """
    print "Splitting Data into Training (80%) and Test (20%) Sets ... ",
    test_ham = bows_ham[:(len(bows_ham) * 20 / 100)]
    Train_ham = bows_ham[(len(bows_ham) * 20 / 100):]
    test_spam = bows_spam[:(len(bows_spam) * 20 / 100)]
    Train_spam = bows_spam[(len(bows_spam) * 20 / 100):]

    X_train = np.append(Train_spam, Train_ham, axis=0)
    X_test = np.append(test_spam, test_ham, axis=0)
    y_train = np.append(np.ones((len(Train_spam), 1)), np.zeros((len(Train_ham), 1)), axis=0)
    y_test = np.append(np.ones((len(test_spam), 1)), np.zeros((len(test_ham), 1)), axis=0)
    print "DONE"
    return X_train, X_test, y_train, y_test


def calculate(X_train, y_train, X_test):
    """ Create, Train Models. Make predictions on test data.

    :param X_train:
    :param y_train:
    :param X_test:
    :return:  y_pred1, y_pred2
    """
    print "Creating Models ...",
    model1 = MultinomialNB()
    model2 = LinearSVC()
    print "DONE"
    print "Training Models ...",
    model1.fit(X_train, y_train)
    model2.fit(X_train, y_train)
    print "DONE"
    print "Making Predictions on Test Data ...",
    y_pred1 = model1.predict(X_test)
    y_pred2 = model2.predict(X_test)
    print "DONE"
    return y_pred1, y_pred2


def result(y_test, y_pred1, y_pred2):
    # 0 = ham, 1 = spam
    """ Show Confusion Matrices based on predictions.

    :param y_test:
    :param y_pred1:
    :param y_pred2:
    """
    print "Confusion Matrices ...\n"
    print "MultinomialNB :"
    print confusion_matrix(y_test, y_pred1, labels=[0, 1])
    u"""[[725   9]
     [ 18 282]]"""
    print "\nLinearSVC :"
    print confusion_matrix(y_test, y_pred2, labels=[0, 1])
    u"""[[713  21]
     [  9 291]]"""


def run():
    ham_name, ham_mail, spam_name, spam_mail = load_dataset()

    # My Way : But it is very slow (200 mail)
    # ############################################################
    # b = Bag_of_Words()
    # b.create_vocabulary(ham_mail[:100] + spam_mail[:100])
    # bows_ham = b.bag_of_words(ham_mail[:100], mode='count')
    # bows_spam = b.bag_of_words(spam_mail[:100], mode='count')
    # ############################################################

    # With Keras : its really good :D (all mail)
    # ############################################################

    t = Tokenizer()
    t.fit_on_texts(ham_mail + spam_mail)
    bows_ham = t.texts_to_matrix(ham_mail, mode='count')
    bows_spam = t.texts_to_matrix(spam_mail, mode='count')
    # ############################################################

    X_train, X_test, y_train, y_test = split(bows_ham, bows_spam)
    y_pred1, y_pred2 = calculate(X_train, y_train, X_test)

    result(y_test, y_pred1, y_pred2)


if __name__ == '__main__':
    run()
