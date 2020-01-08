import spacy
from spacy import displacy

#python -m spacy download en

nlp = spacy.load('en_core_web_sm')
doc = nlp('''I purchased from april 2018 till now there is no technical issue in my bike. 
          This is a excellent bike for daily use with average speed. No maintenance, more than 65/kmpl. 
          I would like to suggest purchase this bike for daily use. This is good looking comfortable riding.
          Good servicing experience in khurda, odisha. All staffs are friendly.''')

for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)