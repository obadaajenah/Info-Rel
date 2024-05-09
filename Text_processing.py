import re
import csv
import enchant
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from num2words import num2words
from collections import Counter
from textblob import TextBlob
import string
from nltk import pos_tag
from nltk.corpus import wordnet
from spellchecker import SpellChecker  # Import spell checker

class TextProcessor:
    def __init__(self):
        self.spell_checker = SpellChecker()

    @staticmethod
    def convert_numbers_to_words(sentence):
        words = sentence.split()
        converted_sentence = []
        for word in words:
            try:
                if word.isdigit():  
                    converted_word = num2words(int(word), lang='en')
                    converted_sentence.append(converted_word)
                else:
                    converted_sentence.append(word)
            except ValueError:
                # If conversion to int fails, just append the word as it is
                converted_sentence.append(word)
        return " ".join(converted_sentence)

    @staticmethod
    def get_wordnet_pos(tag):

        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
    
    @staticmethod
    def cleaning_text(text):
        cleaned_text = re.sub(r'\W', ' ', text) 
        return cleaned_text
    
    @staticmethod
    def Tokenization(text):
        senteances = sent_tokenize(text)  # Tokenize into sentences
        words = []
        for sentence in senteances:
            words.extend(word_tokenize(sentence))
        return words

    @staticmethod
    def Stopword_removal(text):
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in text if word.lower() not in stop_words]
        return filtered_words
    
    @staticmethod
    def Lemmatization(text):
        pos_tags = pos_tag(text)
        # pos_tags = pos_tag(filtered_words)
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word, pos=TextProcessor.get_wordnet_pos(tag)) for word, tag in pos_tags]
        return lemmatized_words

    @staticmethod
    def Stemming(text):
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in text]  # Stem words
        
        return stemmed_words







    @staticmethod
    def correct(text: str | list[str]) -> str | None:
        if isinstance(text, list):
            # Join the list elements into a single string
            text = ' '.join(text)

        # Ensure text is a string before passing it to TextBlob
        if not isinstance(text, str):
            return None

        # Correct the text
        corrected_text = str(TextBlob(text).correct())
        return corrected_text





# Open the TSV file for reading and the output file for writing
with open('D:/Info-Rel/File/collection.tsv', 'r', encoding='utf-8') as input_file, open('preprocessed_collection.tsv', 'w', encoding='utf-8') as output_file:
    # Create a CSV reader for the input file
    reader = csv.reader(input_file, delimiter='\t')
    
    # Create a CSV writer for the output file
    writer = csv.writer(output_file, delimiter='\t')
    
    # Instantiate TextProcessor
    text_processor = TextProcessor()
    
    # Process each row in the TSV file
    for row in reader:
        text = row[1]  # Assuming the text is in the second column (index 1)
        # preprocessed_text = text_processor.preprocess_text(text)
        clean= text_processor.cleaning_text(text)
        tokenize=text_processor.Tokenization(clean)
        Stopword_removal=text_processor.Stopword_removal(tokenize)
        Lemmatizer=text_processor.Lemmatization(Stopword_removal)
        Stemming=text_processor.Stemming(Lemmatizer)



        
        # Convert preprocessed text to a string
        preprocessed_text_str = ' '.join( Stemming)
        
        # Convert numbers to words
        #converted_text = text_processor.convert_numbers_to_words(preprocessed_text_str)
        
        # Correct the text
        #corrected_text = text_processor.correct(converted_text)
        
        # Write the index and corrected text to the output file
        writer.writerow([row[0],  Stemming])




# #Example usage:
# text = """Hellwo My -- ///  :neme obadad and fifteen  this my friend ali_ola usually 5 Abdo playing 8 ?. We also did not live here 10 MOTHERS! ."""
# processor = TextProcessor()
# processed_number = processor.convert_numbers_to_words(text)
# processed_text = processor.preprocess_text(processed_number)
# #processed_spell = processor.spell_check(processed_text)
# processed_correct = processor.correct(processed_text)
# print("text befor processing:",text)
# print("the processed nubmer is:",processed_number)
# print("the processed text :",processed_text)
# print("the processed correct :",processed_correct)

#gggggggggggggg#
