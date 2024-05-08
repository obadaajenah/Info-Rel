
import csv
import json
import csv

class DocumentParser:
    def __init__(self, file_path, delimiter='\t'):
        self.file_path = file_path
        self.delimiter = delimiter

    def parse_documents(self):
        documents = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            for row in reader:
                if len(row) >= 2:
                    doc_id = int(row[0])
                    tokens = [token.strip("' ") for token in row[1][1:-1].split(',')]
                    documents.append((doc_id, tokens))
        return documents

    def save_documents(self, output_file_path):
        documents = self.parse_documents()
        with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
            writer = csv.writer(output_file, delimiter=self.delimiter)
            for doc_id, tokens in documents:
                writer.writerow([doc_id, tokens])

# Example usage:
parser = DocumentParser('preprocessed_collection.tsv')
output_file_path = 'parsed_collection.tsv'
parser.save_documents(output_file_path)
print(f"Parsed documents saved to {output_file_path}")