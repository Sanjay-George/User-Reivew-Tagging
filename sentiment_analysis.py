import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords

## ONE TIME
#nltk.download("stopwords")


#posAdj = ['good', 'easy', 'awesome', 'super', 'decent', 'powerful', 'wonderful', 'excellent', 'best', 'comfortable']
#negAdj = ['bad', 'tough', 'awful', 'lacking']
#intensifiers = ['very', 'really', 'extremely', 'absolutely', 'completely', 'quite', 'totally', 'highly']
#posSup = ['best', 'easiest', 'most']
#negSup = ['least', 'worst']
negations = ['no', 'not', 'doesn\'t', 'don\'t']
sentenceSep = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'also', '.', ';', ',', '-'] 
htmlRegex = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

dataset = pd.read_csv("./datasets/bikewale/Reviews.csv", error_bad_lines=False, sep="\t", quoting=3)
dataset = dataset.dropna().reset_index(drop=True)

# FETCH KEYWORDS FROM DATABASE
keywords = ['bike', 'year', 'experience', 'thing', 'mileage', 'love', 'drive', 'seat', 'handling', 'performance', 'look', 'comfort', 'say', 'riding', 'segment', 'buying', 'buy', 'service', 'maintenance', 'compared', 'buying experience', 'using', 'cost', 'power', 'ride', 'speed', 'pick', 'vehicle', 'time', 'bought', 'feel', 'gear', 'month', 'got', 'kmpl', 'want', 'vibration', 'problem', 'ab', 'price', 'give', 'make', 'come', 'fuel', 'start', 'feature', 'lot', 'scooter', 'money', 'tv', 'scooty', 'pickup', 'kmph', 'km', 'bit', 'body', 'think', 'servicing', 'city', 'riding experience', 'bike bike', 'traffic', 'road', 'use', 'hero', 'engine', 'style', 'pulsar', 'rider', 'get', 'issue', 'day', 'oil', 'change', 'brake', 'need', 'look performance', 'honda', 'ride bike', 'range', 'showroom', 'sport', 'suspension', 'value', 'yamaha', 'bike look', 'take', 'friend', 'bajaj', 'design', 'people', 'look bike', 'highway', 'tyre', 'company', 'bike ride', 'enfield', 'would', 'buy bike', 'activa']

# FETCH POS AND NEG ADJECTIVES FROM DB (OR FROM FILE)
pos_adj = set(pd.read_csv("./datasets/adjectives/positive_adjectives.txt", error_bad_lines=False, sep="\t", quoting=3, header=None, names=['word']).word)
neg_adj = set(pd.read_csv("./datasets/adjectives/negative_adjectives.txt", error_bad_lines=False, sep="\t", quoting=3, header=None, names=['word']).word)


#TODO : 
#    1. find indices of all sentence separators in a review
#    2. If any adjacent sentenceSep, then take only the last one
#    3. Divide sentence into subsentences based on the indices 
#    4. if any subsentence has just one word, merge with previous sub
#    5. Do further analysis

#FOR ONE REVIEW
review = re.sub('[^a-zA-Z.,;-]', ' ', dataset['Review'][12])
sub_sentences = review.lower().split(".")
sub_sentences = [s.strip() for s in sub_sentences if len(s) > 5]
temp_subs = []
sub_sentences = [temp_subs.append(s.split(",")) for s in sub_sentences]

# once splitting is done
for sentence in sub_sentences:
    if 'mileage' in sentence:
        print("milege found")
        sentence = sentence.split()
        for word in sentence :
            if word in negations:
                print('negate the meaning')
            elif word in pos_adj:
                print("mileage positive")
            elif word in neg_adj:
                print("mileage negative")
        




##for i in range(len(dataset)):
#review = re.sub(htmlRegex, ' ', dataset['Review'][1])  # to clean html tags
#subsentences = review.lower().split(',')
#for sentence in subsentences:    
#    print(sentence)
#    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
#    sentence = sentence.lower().split()
#    sentence = [word for word in sentence if len(word) > 1]
#    print(sentence)
#

# TODO : 
#1. split into sub sentences
#2. foreach subsentence check if any feature (foreach feature)
#if present :
#a. check for negatives -> polarity reversed
#b. check superlative
#c. check intensifier 
#d. check other adjectives
