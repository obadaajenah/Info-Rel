import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from num2words import num2words
from spellchecker import SpellChecker  # Import spell checker

class TextProcessor:
    def __init__(self):
        self.spell_checker = SpellChecker()

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

    def preprocess_text(self, text):
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
        
        # Lemmatization and Spell Checking
        lemmatizer = WordNetLemmatizer()
        spell_checked_words = []
        for word in filtered_words:
            lemmatized_word = lemmatizer.lemmatize(word)
            corrected_word = self.spell_check_word(lemmatized_word)  # Use self.spell_checker
            if corrected_word:
                spell_checked_words.append(corrected_word)
        
        # Stemming
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in spell_checked_words]  # Stem words
        
        return stemmed_words
    
    def spell_check_word(self, word):
        # Use self.spell_checker to correct word
        return self.spell_checker.correction(word)

#hhh
# Example usage:
text = """Hellwo My -- ///  :name obadad and fifteen  this my freind ali_ola usully 5 Abdo playing 8 ?. We also did not live here 10 MOTHERS! ."""
processor = TextProcessor()
processed_number = processor.convert_numbers_to_words(text)
processed_text = processor.preprocess_text(processed_number)

print("Original text before processing:", text)
print("Processed number:", processed_number)
print("Processed text after preprocessing:", processed_text)
