
from Text_processing import TextProcessor  
print("fffffffffffff")

# إنشاء كائن من الكلاس TextProcessor
text_processor = TextProcessor()

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found!")

def process_query(file_path):
    query = read_file(file_path)
    # query= "i am stading with my group"
    clean = text_processor.cleaning_text(query)
    tokenize = text_processor.Tokenization(clean)
    Stopword_removal = text_processor.Stopword_removal(tokenize)
    corrected=text_processor.correct(Stopword_removal)
    Lemmatizer = text_processor.Lemmatization(corrected)
    Stemming = text_processor.Stemming(Lemmatizer)
    print( Stemming)
    return  Stemming  

# # استدعاء الدالة لقراءة الملف النصي
file_path = 'ff.txt'
process_query(file_path)