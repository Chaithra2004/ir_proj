from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class NewsIndexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(tokenizer=lambda x: x,
                                        preprocessor=lambda x: x,
                                        token_pattern=None)
        self.tfidf_matrix = None
        self.documents = []
        self.doc_ids = []

    def build_index(self, processed_documents, doc_ids):
        """
        Build TF-IDF index for the processed documents
        """
        self.documents = processed_documents
        self.doc_ids = doc_ids
        
        # Convert preprocessed tokens back to strings for vectorizer
        doc_strings = [' '.join(doc) for doc in processed_documents]
        self.tfidf_matrix = self.vectorizer.fit_transform(doc_strings)
        
    def get_feature_names(self):
        """
        Get the vocabulary of the vectorizer
        """
        return self.vectorizer.get_feature_names_out()

    def get_document_vector(self, doc_idx):
        """
        Get the TF-IDF vector for a specific document
        """
        return self.tfidf_matrix[doc_idx]

    def compute_query_vector(self, processed_query):
        """
        Compute TF-IDF vector for a query
        """
        query_string = ' '.join(processed_query)
        return self.vectorizer.transform([query_string])
