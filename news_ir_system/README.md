# News Information Retrieval System

This project implements a news information retrieval system that processes JSON news data files and retrieves relevant articles based on user queries. The system uses TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity for ranking search results.

## Features

- JSON data file processing
- Text preprocessing (tokenization, stopword removal)
- TF-IDF vectorization
- Cosine similarity-based ranking
- Query processing and result retrieval

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Download NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage

1. Place your JSON news data files in the `data` directory
2. Run the main script:
```bash
python news_ir.py
```

3. Enter your search query when prompted

## Project Structure

- `news_ir.py`: Main IR system implementation
- `preprocessor.py`: Text preprocessing utilities
- `indexer.py`: TF-IDF indexing implementation
- `searcher.py`: Search and ranking functionality
- `data/`: Directory for JSON news data files
