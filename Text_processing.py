
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


class TextProcessor:
    def __init__(self):
        pass

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
    def preprocess_text(text):
        # Convert numbers to words
        text = TextProcessor.convert_numbers_to_words(text)
        
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
    @staticmethod
    def spell_check(words):
        # Load custom dictionary
        with open("custom_dictionary.txt", "r") as f:
            custom_dictionary = set(word.strip() for word in f.readlines())
        
        # Punctuation removal
        words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

        # Count occurrences of each word
        word_counts = Counter(words)

        # Initialize error dictionary
        error_dict = {}

        # Iterate through words
        for word, count in word_counts.items():
            # Check if word is in custom dictionary or is a number
            if word not in custom_dictionary and not word.isdigit():
                # For simplicity, let's just include the word itself as the correction
                # You can replace this with more sophisticated correction algorithms
                # such as Levenshtein distance or edit distance
                error_dict[word] = [word]

        return error_dict

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
        preprocessed_text = text_processor.preprocess_text(text)
        
        # Convert preprocessed text to a string
        preprocessed_text_str = ' '.join(preprocessed_text)
        
        # Convert numbers to words
        #converted_text = text_processor.convert_numbers_to_words(preprocessed_text_str)
        
        # Correct the text
        #corrected_text = text_processor.correct(converted_text)
        
        # Write the index and corrected text to the output file
        writer.writerow([row[0], preprocessed_text])




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