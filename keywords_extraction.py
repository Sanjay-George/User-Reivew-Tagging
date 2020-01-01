import numpy as np
import pandas as pd

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet as wn

dataset = pd.read_csv("./datasets/bikewale/combined.txt", sep="\t", quoting=3)


# one time download
nltk.download("stopwords")
nltk.download('wordnet')
    
# lemmatizer - alternative to stemmer
lemma = nltk.wordnet.WordNetLemmatizer()    
stopwords = set(nltk.corpus.stopwords.words('english'))
#adjs = set(wn.all_synsets(wn.ADJ))
#nouns = set(wn.all_synsets(wn.NOUN))

# adjExceptions = ['front', 'back', 'rear']   ?? CHECK IF REQD.
# fetch some ignore words from DB too (bike, driver, honda, make names, etc)
htmlRegex = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
removeWordsTemp = set(['r', 'n', 'f', 'e', 'em', 'amp', ''])
corpus = []

for i in range (0, len(dataset)):
    review = re.sub(htmlRegex, ' ', dataset['Review'][i])  # to clean html tags
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower().split()
    review = [word for word in review if not word in stopwords]
    review = [lemma.lemmatize(word) for word in review]
    review = [word for word in review if not word in removeWordsTemp]  ## handling bad data (html format)
    review_temp = []
    for word in review:
        if len(wn.synsets(word, pos='a')) == 0 and len(wn.synsets(word, pos='r')) == 0:
            review_temp.append(word)
#        else:
#            if (len(wn.synsets(word, pos='n')) > 0):
#                review_temp.append(word)
    review = review_temp         
    review = ' '.join(review)
    corpus.append(review)   


# bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=50, ngram_range=(1, 2), analyzer='word')
X = cv.fit_transform(corpus).toarray()
vocab = cv.vocabulary_
print(vocab.keys())

## TF IDF WEIGHTING 
#from sklearn.feature_extraction.text import TfidfTransformer
#tf = TfidfTransformer()
#X2 = tf.fit_transform(X).toarray()   # transforming vector formed by Count Vectorizer to TF IDF format
#
#tf.idf_


## remove stopwords 
## porter stemming 
#corpus = []
#ps = PorterStemmer()
#for i in range (0, len(dataset)):
#    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
#    review = review.lower().split()
#    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
#    review = ' '.join(review)
#    corpus.append(review)
    


# REMOVE ADJECTIVES 
# REMOVE TERMS LIKE CARS, DRIVER, VEHICLES ETC