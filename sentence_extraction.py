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

Reviews = dataset['Review']

for review in Reviews:
    mod_review = ""    
    # CHECK SEPARATORS
    for char in review :
        if char in set(separators):
            mod_review = mod_review + "$"
        else :
            mod_review = mod_review + char
            
    review = mod_review.split()
    mod_review = []
    # CHECK CONJUNCTIONS
    for word in review:
        if re.sub('a-zA-Z', '', word.lower()) in set(conjunctions):
            mod_review.append("$")
        else:
            mod_review.append(word)
    
    review = ' '.join(mod_review)
    sub_sentences = [sentence for sentence in review.split("$") if len(sentence.strip()) > 1]

# TAKES 10s FOR 36,000 REVIEWS

