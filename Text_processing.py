
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from num2words import num2words

class TextProcessor:
    def __init__(self):
        pass

    @staticmethod
    def convert_numbers_to_words(sentence):
        words = sentence.split()
        converted_sentence = []
        for word in words:
            if word.isdigit():  
                converted_word = num2words(int(word), lang='en')
                converted_sentence.append(converted_word)
            else:
                converted_sentence.append(word)
        return " ".join(converted_sentence)

    @staticmethod
    def preprocess_text(text):
        # Cleaning
        cleaned_text = re.sub(r'\W', ' ', text)  # Remove unwanted characters
        
        # Tokenization
        sentences = sent_tokenize(cleaned_text)  # Tokenize into sentences
        words = []
        for sentence in sentences:
            words.extend(word_tokenize(sentence))  # Tokenize into words
        
        # Stopword removal
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word.lower() not in stop_words]  # Remove stopwords
        
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]  # Lemmatize words
        
        # Stemming
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in lemmatized_words]  # Stem words
        
        return stemmed_words


# Example usage:
text = """Hellwo My -- ///  :name obadad and fifteen  this my friend ali_ola usually 5 Abdo playing 8 ?. We also did not live here 10 MOTHERS! ."""
processor = TextProcessor()
processed_number = processor.convert_numbers_to_words(text)
processed_text = processor.preprocess_text(processed_number)
print("text befor processing:",text)
print("the processed nubmer is:",processed_number)
print("the processed text :",processed_text)

#gggggggggggggg#