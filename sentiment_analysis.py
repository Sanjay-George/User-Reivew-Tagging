import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords

## ONE TIME
#nltk.download("stopwords")

negations = ['no', 'not', 'doesn\'t', 'don\'t']
conjunctions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'also']
separators = ['.', ';', ',', '-'] 
htmlRegex = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

dataset = pd.read_csv("./datasets/bikewale/Reviews.csv", error_bad_lines=False, sep="\t", quoting=3)
dataset = dataset.dropna().reset_index(drop=True)

# FETCH KEYWORDS FROM DATABASE
keywords = set(['bike', 'year', 'experience', 'thing', 'mileage', 'love', 'drive', 'seat', 'handling', 'performance', 'look', 'comfort', 'say', 'riding', 'segment', 'buying', 'buy', 'service', 'maintenance', 'compared', 'buying experience', 'using', 'cost', 'power', 'ride', 'speed', 'pick', 'vehicle', 'time', 'bought', 'feel', 'gear', 'month', 'got', 'kmpl', 'want', 'vibration', 'problem', 'ab', 'price', 'give', 'make', 'come', 'fuel', 'start', 'feature', 'lot', 'scooter', 'money', 'tv', 'scooty', 'pickup', 'kmph', 'km', 'bit', 'body', 'think', 'servicing', 'city', 'riding experience', 'bike bike', 'traffic', 'road', 'use', 'hero', 'engine', 'style', 'pulsar', 'rider', 'get', 'issue', 'day', 'oil', 'change', 'brake', 'need', 'look performance', 'honda', 'ride bike', 'range', 'showroom', 'sport', 'suspension', 'value', 'yamaha', 'bike look', 'take', 'friend', 'bajaj', 'design', 'people', 'look bike', 'highway', 'tyre', 'company', 'bike ride', 'enfield', 'would', 'buy bike', 'activa'])

# FETCH POS AND NEG ADJECTIVES FROM DB (OR FROM FILE)
pos_adj = set(pd.read_csv("./datasets/adjectives/positive_adjectives.txt", error_bad_lines=False, sep="\t", quoting=3, header=None, names=['word']).word)
neg_adj = set(pd.read_csv("./datasets/adjectives/negative_adjectives.txt", error_bad_lines=False, sep="\t", quoting=3, header=None, names=['word']).word)


review = dataset['Review'][520]
mod_review = ""

for char in review :
    if char in set(separators):
        mod_review = mod_review + "$"
    else :
        mod_review = mod_review + char
        

review = mod_review.split()
mod_review = []
for word in review:
    if re.sub('a-zA-Z', '', word.lower()) in set(conjunctions):
        mod_review.append("$")
    else:
        mod_review.append(word)

review = ' '.join(mod_review)
sub_sentences = [sentence for sentence in review.split("$") if len(sentence.strip()) > 1]






#sentences = [s.strip() for s in sentences if len(s) > 5]
#temp_subs = []
#sentences = [temp_subs.append(s.split(",")) for s in sentences]

# once splitting is done
for sentence in sentences:
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
