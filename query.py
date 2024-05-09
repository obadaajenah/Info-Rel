
from Text_processing import TextProcessor  


# إنشاء كائن من الكلاس TextProcessor
text_processor_obj = TextProcessor()

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
    Lemmatizer = text_processor.Lemmatization(Stopword_removal)
    Stemming = text_processor.Stemming(Lemmatizer)
    print( Stemming)
    return  Stemming  

# استدعاء الدالة لقراءة الملف النصي
file_path = 'ff.txt'
process_query(file_path)