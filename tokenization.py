
# TOKENIZATION

# IMPORTING LIBRARIES
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer

# DEFINING SAMPLE TEXTS
text1 =  "Hello World.This is the first tokenizing example"
text2 = "Hey it's me. Check this out."

# SENTENCE TOKENIZING
sentences1 = sent_tokenize(text1)
sentences2 = sent_tokenize(text2)

print(sentences1,"\n",sentences2)

# WORD TOKENIZING (TOKENIZING THE TEXTS SEPARATED BY SPACES) 
tokenizer = RegexpTokenizer('\s+',gaps=True)
print("For Text 1:",tokenizer.tokenize(text1),"\nFor Text 2:",tokenizer.tokenize(text2))


# TRYING A LARGE DATASET

f = open("sample_text.txt","r")
x = f.read()


print(tokenizer.tokenize(x))

f.close()