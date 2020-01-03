import numpy as np
import pandas as pd

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet as wn

#dataset = pd.read_csv("./datasets/bikewale/combined.txt", sep="\t", quoting=3)
dataset = pd.read_csv("./datasets/bikewale/Reviews.csv", error_bad_lines=False,sep="\t", quoting=3)
dataset = dataset.dropna().reset_index(drop=True)

# SENTIMENT DATASET FROM SENTIC4NET
sentiment = pd.read_csv('./datasets/adjectives/senticnet4.txt', sep="\t", error_bad_lines=False, quoting=3, header=None, names=['word', 'polarity', 'score'])
sentiment = sentiment.dropna().reset_index(drop=True)
pos_dataset = set(sentiment[sentiment.score > 0].word)
neg_dataset = set(sentiment[sentiment.score < 0].word)


lemma = nltk.wordnet.WordNetLemmatizer()    
stopwords = set(nltk.corpus.stopwords.words('english'))

# adjExceptions = ['front', 'back', 'rear']   ?? CHECK IF REQD.
# fetch some ignore words from DB too (bike, driver, honda, make names, etc)
htmlRegex = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
ignoreWords = set(['r', 'n', 'f', 'e', 'em', 'amp', '', 'le'])
corpus = []

pos_adjectives = set()
neg_adjectives = set()


for i in range (0, len(dataset)):
    review = re.sub(htmlRegex, ' ', dataset['Review'][i])  # to clean html tags
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower().split()
    review = [word for word in review if not word in stopwords]
    review = [lemma.lemmatize(word) for word in review]
    review = [word for word in review if not word in ignoreWords]  ## handling bad data (html format)
    for word in review:
        if len(wn.synsets(word, pos='a')) > 0:   
            if word in pos_dataset:
                pos_adjectives.add(word)
            elif word in neg_dataset:
                neg_adjectives.add(word)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                