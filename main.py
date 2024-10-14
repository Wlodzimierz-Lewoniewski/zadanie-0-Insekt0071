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

def main():
    # number of documents
    n = int(input("Enter the number of documents: ").strip())
    
    # documents
    documents = []
    for i in range(n):
        document_content = input(f"Enter content of document {i + 1}: ").strip()
        documents.append(document_content)
    
    # number of queries
    m = int(input("Enter the number of queries: ").strip())
    
    # queries
    queries = []
    for i in range(m):
        query = input(f"Enter query {i + 1}: ").strip().lower()
        queries.append(query)
    
    results = process_documents(n, documents, m, queries)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
