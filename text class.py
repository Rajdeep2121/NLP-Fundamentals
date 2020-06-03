
# TEXT CLASS

# IMPORTING LIBRARIES
import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

words = [word.lower() for word in movie_reviews.words()]
print(words[:10])
print("Number of total words:",len(words))

# GETTING THE DICTIONARY HAVING ALL THE WORDS WITH THEIR FREQUENCIES
dictWords = nltk.FreqDist(words)
dictWords

print("No of distinct words in this text including all punctuations are:",len(dictWords))

# TO FIND THE NUMBER OF OCCURENCES OF A PARTICULAR WORD IN THE TEXT 
print("No of times 'good' occured:",dictWords["good"])
print("No of times 'boring' occured:",dictWords["boring"])
print("No of times 'bad' occured:",dictWords["bad"])