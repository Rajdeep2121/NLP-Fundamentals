
# STOP WORDS FILTERING

# IMPORTING LIBRARIES
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# SAMPLE TEXT
text = "I have a meeting scheduled at tommorrow morning at 7:30 sharp."

# TOKENIZING WORDS
words = word_tokenize(text)

# CREATING LIST OF STOPWORDS IN ENGLISH 
stop_words = set(stopwords.words("english"))

l = [w for w in words if w not in stop_words]
print(l)

# REMOVING PUNCTUATIONS

# NEW EXAMPLE 
sample_text1 = "The boy was happy… at the start of his summer holiday."
sample_text2 = "We set out at dawn; the weather looked promising."

# REMOVING PUNCTUATIONS 
tokenizer = nltk.RegexpTokenizer(r'\w+')
new_words1 = tokenizer.tokenize(sample_text1)
new_words2 = tokenizer.tokenize(sample_text2)

print(new_words1)
print(new_words2)