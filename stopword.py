import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#nltk.download()
text="""Hellwo My -- ///  name obadad and this my friend Abdo. we also live here."""

stop_words = set(stopwords.words('english'))
#print(stop_words)

#def remove_stop_words(words):
 #   stop_words = stopwords.words('english')
  #  return [w for w in words if w not in stop_words]

tokenize_words = word_tokenize(text)
tokenize_words_without_stop_words = []
for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)

print(set(tokenize_words)-set(tokenize_words_without_stop_words))
print(tokenize_words_without_stop_words)

###########ola and bayan ###########

