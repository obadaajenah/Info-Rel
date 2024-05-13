from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
from query import process_query
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
class IndexBuilder:
    def __init__(self):
        self.index = defaultdict(list)

    def build_index(self, documents):
        for doc_id, tokens in documents:
            for token in tokens:
                self.index[token].append(doc_id)

    def save_index(self, output_file_path):
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for term, postings in self.index.items():
                output_file.write(f"{term}\t{','.join(map(str, postings))}\n")

# Example usage:
index_builder = IndexBuilder()
documents = [
    (0, ['experi', 'rabbit', 'easi', 'housebreak', ...]),  # Example document data
    (1, ['rabbit', 'easili', 'train', 'use', 'litter', ...]),  # Example document data
    # Add more documents here if needed
]


# Read the parsed collection from the file
parsed_documents = []

with open('parsed_collection.tsv', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split('\t')
        doc_id = int(parts[0])
        tokens = parts[1].split(',')
        parsed_documents.append((doc_id, tokens))

# Extract the preprocessed text from the document data and join tokens into strings
preprocessed_texts = [' '.join(tokens) for _, tokens in parsed_documents ]
q=process_query("ff.txt")
print(q)
# Initialize the TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer to your preprocessed documents and transform them into TF-IDF vectors
tfidf_vectors = tfidf_vectorizer.fit_transform(preprocessed_texts)
query_vector = tfidf_vectorizer.transform(q)
# Define the output file path
output_file_path = 'tfidf_vectors.csv'
print(tfidf_vectors)
print(query_vector)
similarities = cosine_similarity(query_vector, tfidf_vectors)
print(similarities)
sorted_indices = np.argsort(similarities[0])[::-1] 
# Convert the query vector to a list of TF-IDF values
top_results = sorted_indices[:3]  # الحصول على أعلى 3 نتائج، على سبيل المثال

print("Max Result")
for i, idx in enumerate(top_results):
    print(f"Doc {idx+1}: {similarities[0][idx]}")
query_vector_file_path = 'query_vector.pkl'
doc_vector_file_path = 'doc_vector.pkl'

# Save the query vector to a binary file using pickle
with open(query_vector_file_path, 'wb') as output_file:
    pickle.dump(query_vector, output_file)

with open(doc_vector_file_path, 'wb') as output_file:
    pickle.dump(tfidf_vectors, output_file)


# Save the TF-IDF vectors to a CSV file
# with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerow(['Document ID'] + tfidf_vectorizer.get_feature_names_out())  # Write header row
#     for doc_id, tfidf_vector in zip(parsed_documents, tfidf_vectors):
#         writer.writerow([doc_id] + tfidf_vector.toarray().tolist()[0])



# index_builder.build_index(parsed_documents)
# output_index_file_path = 'index.txt'
# index_builder.save_index(output_index_file_path)
# print(f"Index saved to {output_index_file_path}")