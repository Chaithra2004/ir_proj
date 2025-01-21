import json
import os
from preprocessor import TextPreprocessor
from indexer import NewsIndexer
from searcher import NewsSearcher

class NewsIRSystem:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.indexer = NewsIndexer()
        self.searcher = NewsSearcher(self.indexer)
        self.documents = {}

    def load_json_files(self, data_dir):
        """
        Load and process JSON news files from the data directory
        """
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        news_data = json.loads(content)
                        if isinstance(news_data, list):
                            for item in news_data:
                                # Use link as unique ID
                                doc_id = item['link']
                                self.documents[doc_id] = item
                        else:
                            doc_id = news_data['link']
                            self.documents[doc_id] = news_data
                except Exception as e:
                    print(f"Error loading {filename}: {str(e)}")
                    continue

    def build_index(self):
        """
        Build the search index from loaded documents
        """
        processed_docs = []
        doc_ids = []
        
        for doc_id, doc in self.documents.items():
            # Combine headline and short description for indexing
            text_content = f"{doc['headline']} {doc['short_description']}"
            processed_doc = self.preprocessor.preprocess(text_content)
            processed_docs.append(processed_doc)
            doc_ids.append(doc_id)
        
        self.indexer.build_index(processed_docs, doc_ids)

    def search(self, query, top_k=10):
        """
        Search for news articles matching the query
        """
        # Preprocess the query
        processed_query = self.preprocessor.preprocess(query)
        
        # Get search results
        results = self.searcher.search(processed_query, top_k)
        
        # Format results
        formatted_results = []
        for result in results:
            doc = self.documents[result['doc_id']]
            formatted_results.append({
                'headline': doc['headline'],
                'short_description': doc['short_description'],
                'category': doc['category'],
                'score': result['score'],
                'date': doc['date'],
                'link': doc['link']
            })
        
        return formatted_results

def main():
    # Initialize the IR system
    ir_system = NewsIRSystem()
    
    # Create data directory if it doesn't exist
    data_dir = 'Data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created {data_dir} directory. Please add your JSON news files there.")
        return

    # Load and index documents
    print("Loading and indexing documents...")
    ir_system.load_json_files(data_dir)
    
    if not ir_system.documents:
        print("No JSON files found in the data directory.")
        return
        
    ir_system.build_index()
    print(f"Indexed {len(ir_system.documents)} documents.")

    # Interactive search loop
    while True:
        query = input("\nEnter your search query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
            
        results = ir_system.search(query)
        
        if not results:
            print("No matching documents found.")
        else:
            print("\nSearch Results:")
            for i, result in enumerate(results, 1):
                print(f"\n{i}. {result['headline']}")
                print(f"   {result['short_description']}")
                print(f"   Category: {result['category']}")
                print(f"   Date: {result['date']}")
                print(f"   Score: {result['score']:.4f}")
                print(f"   Link: {result['link']}")

if __name__ == "__main__":
    main()
