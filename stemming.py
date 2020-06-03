
# STEMMING

# IMPORTING LIBRARIES
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# PORTER STEMMER
# IMPLEMENTATION OF PORTER STEMMER
ps = PorterStemmer()
lst = ['playing','player','played','playful','likes','likely','liked','liking']

# RESULTS OF STEMMING
for word in lst:
    print(word,"=>",ps.stem(word))

# FUTURE WORKS
"""
Implementation of different stemmers like Lancaster Stemmer, SnowBall Stemmer, Lovins Stemmer, Dawson Stemmer
"""