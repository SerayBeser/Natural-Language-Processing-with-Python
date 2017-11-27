""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil Isleme

**** Simple Sentiment Analysis  ****
**** Basit Duygu Analizi ****
"""

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from afinn import Afinn


def sentiment_with_TextBlob(text):
    sentiments = list()
    for sentence in text.sentences:
        sentiments.append(sentence.sentiment)
    return sentiments


def sentiment_with_naive_bayes(train, test, text):
    cl = NaiveBayesClassifier(train)
    accuracy_ = cl.accuracy(test)
    class_ = cl.classify(text)
    return accuracy_, class_


def sentiment_affin(text):
    afinn = Afinn()
    score = afinn.score(text)
    return score


def demo():
    train = [('I love this car', 'positive'),
             ('This view is amazing', 'positive'),
             ('I feel great this morning', 'positive'),
             ('I do not like this car', 'negative'),
             ('This view is horrible', 'negative'),
             ('I feel tired this morning', 'negative')

             ]

    test = [
        ('I am so excited about the concert', 'positive'),
        ('He is my best friend', 'positive'),
        ('I am not looking forward to the concert', 'negative'),
        ('He is my enemy', 'negative')
    ]

    print "Sentiment with TextBlob"
    sentiments = sentiment_with_TextBlob(text=TextBlob("Hi, I watch an amazing film."))
    print sentiments

    print "\nSentiment with TextBlob, Naive Bayes classifier"
    accuracy_, class_ = sentiment_with_naive_bayes(train, test, text="Hi, I watch an amazing film.")
    print accuracy_, class_

    print "\nSentiment with Affin"
    score = sentiment_affin(text="Hi, I watch an amazing film.")
    print score


if __name__ == '__main__':
    demo()
