from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class NewsSearcher:
    def __init__(self, indexer):
        self.indexer = indexer

    def search(self, processed_query, top_k=10):
        """
        Search for relevant documents using cosine similarity
        """
        # Get query vector
        query_vector = self.indexer.compute_query_vector(processed_query)
        
        # Compute cosine similarity between query and all documents
        similarities = cosine_similarity(query_vector, self.indexer.tfidf_matrix).flatten()
        
        # Get top-k document indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Create search results
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:  # Only include relevant documents
                results.append({
                    'doc_id': self.indexer.doc_ids[idx],
                    'score': float(similarities[idx])
                })
        
        return results
