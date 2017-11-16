""" @SerayBeser

Natural Language Processing with Python

Python ile Dogal Dil isleme

**** Word Embeddings (Word2Vec wit GenSim)  ****

Word embedding is the collective name for a set of language modeling
and feature learning techniques in natural language processing (NLP)
where words or phrases from the vocabulary are mapped to vectors of
real numbers. Conceptually it involves a mathematical embedding from
a space with one dimension per word to a continuous vector space with
much lower dimension.
Methods to generate this mapping include neural networks, dimensionality
reduction on the word co-occurrence matrix, probabilistic models, and
explicit representation in terms of the context in which words appear.
Word and phrase embeddings, when used as the underlying input representation,
have been shown to boost the performance in NLP tasks such as syntactic
parsing and sentiment analysis. https://en.wikipedia.org/wiki/Word2vec


Word Embedding Algorithms
1. Embedding Layer
2. Word2Vec :  Word2vec is a group of related models that are used to produce word embeddings.
               Word2Vec kelimeler arasindaki uzakligi vektorel olarak hesaplamayi saglar.
--Continuous Bag-of-Words, or CBOW model.
--Continuous Skip-Gram Model.
3. GloVe


"""
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from nltk.corpus import gutenberg
from nltk import sent_tokenize
from preprocessing import cleaning_and_stemming
import matplotlib.pyplot as plt


def word_2_vec_with_gensim(sentences):
    sentences = [cleaning_and_stemming(sent, stemming=False) for sent in sentences]
    model = Word2Vec(sentences, min_count=1)
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    plt.scatter(result[:, 0], result[:, 1])
    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    plt.show()
    print "Death, life similarity :", model.wv.similarity('death', 'life')
    return model


def demo():
    """ LOAD DATA , veri setini yukleyelim.
        """
    # Sense and Sensibility by Jane Austen 1811
    text = gutenberg.raw('austen-sense.txt')
    sentences = sent_tokenize(text[:1000])
    modal = word_2_vec_with_gensim(sentences)
    print "Modal : ", modal


if __name__ == '__main__':
    demo()
