import string
from collections import defaultdict

def clean_word(word):
    return word.strip(string.punctuation).lower()

def process_documents(n, documents, m, queries):
    word_to_docs = defaultdict(lambda: defaultdict(int))
    
    for i in range(n):
        words = documents[i].split()
        for word in words:
            cleaned_word = clean_word(word)
            if cleaned_word:
                word_to_docs[cleaned_word][i] += 1
    
    result = []
    for query in queries:
        cleaned_query = clean_word(query)
        if cleaned_query in word_to_docs:
            doc_freq_list = list(word_to_docs[cleaned_query].items())
            doc_freq_list.sort(key=lambda x: (-x[1], x[0]))
            result.append([doc_idx for doc_idx, _ in doc_freq_list])
        else:
            result.append([]) 
    return result

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    
    documents = [file.readline().strip() for _ in range(n)]
    m = int(file.readline().strip())
    
    queries = [file.readline().strip() for _ in range(m)]

results = process_documents(n, documents, m, queries)

#zapis na koniec
with open('output.txt', 'w') as output_file:
    for res in results:
        output_file.write(f"{res}\n")
