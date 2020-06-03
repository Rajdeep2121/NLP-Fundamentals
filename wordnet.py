# WORDNET

# IMPORTING LIBRARIES
import nltk
from nltk.corpus import wordnet

word = wordnet.synsets("bad")

# DEFINITION OF THE WORD
print(word[0].definition())

# EXAMPLES IN SENTENCES
print(word[0].examples())

# SYNONYMS AND ANTONYMS

antonyms = []
synonyms = []
for i in word:
    for l in i.lemmas():
        synonyms.append(l.name())
        if(l.antonyms()):
            antonyms.append(l.antonyms()[0].name())


# REMOVING DUPLICATES
print("Synonyms:",list(set(synonyms)))
print("Antonyms:",list(set(antonyms)))

# SIMILARITY MEASURE BETWEEN TWO WORDS 

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cruise.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("mouse.n.01")

print(w1.wup_similarity(w2))