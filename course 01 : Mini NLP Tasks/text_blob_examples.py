from textblob import TextBlob, Word

text = TextBlob("John likes to watch movies. Mary likes movies too. These are amazing movies. ")

print "Tags            : ", text.tags  # nltk -> pos_tag
print "Noun Phrases    : ", text.noun_phrases  # whic are 'NNP', 'NNI'
print "Sentences       : ", text.sentences
print "Words           : ", text.words
for sentence in text.sentences:
    print sentence,
    print "Sentiment :", sentence.sentiment

print "dogs, lemmatize : ", Word('dogs').lemmatize()
print "Translate to TR : ", text.translate(to='tr')
