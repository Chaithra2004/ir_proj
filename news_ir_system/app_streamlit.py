import streamlit as st
from news_ir import NewsIRSystem
import pandas as pd
from datetime import datetime

# Configure the Streamlit page
st.set_page_config(
    page_title="News Search Engine",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize the IR system
@st.cache_resource
def initialize_ir_system():
    ir_system = NewsIRSystem()
    data_dir = 'Data'
    ir_system.load_json_files(data_dir)
    ir_system.build_index()
    return ir_system

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Search container */
    .search-container {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    /* Article card styling */
    .article-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border: 1px solid #e0e0e0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .article-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    /* Badge styling */
    .category-badge {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .score-badge {
        background: linear-gradient(45deg, #2196F3, #1976D2);
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Link styling */
    .article-link {
        color: #2196F3;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    .article-link:hover {
        color: #1976D2;
        text-decoration: underline;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
    }
    
    .css-1d391kg .stMarkdown {
        color: white;
    }
    
    /* Custom metric styling */
    .metric-card {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .stTextInput > div > div > input {
        border-radius: 25px;
        padding: 1rem 1.5rem;
        font-size: 1.1rem;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #2196F3;
        box-shadow: 0 0 0 2px rgba(33,150,243,0.2);
    }
    
    h1 {
        color: #1a237e;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #1a237e;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header section
st.markdown('<div class="search-container">', unsafe_allow_html=True)
st.title("📰 News Search Engine")
st.markdown("Discover relevant news articles using natural language search")

# Initialize the IR system
ir_system = initialize_ir_system()

# Search interface with placeholder
query = st.text_input(
    "",
    placeholder="Try searching for 'covid vaccines' or 'airline incidents'...",
    key="search_query"
)

st.markdown('</div>', unsafe_allow_html=True)

if query:
    results = ir_system.search(query)
    
    if not results:
        st.error("🔍 No matching articles found. Try different search terms!")
    else:
        st.success(f"🎯 Found {len(results)} relevant articles")
        
        # Display results in a grid
        cols = st.columns(2)
        for idx, result in enumerate(results):
            with cols[idx % 2]:
                # Parse and format the date
                try:
                    date_obj = datetime.strptime(result['date'], '%Y-%m-%d')
                    formatted_date = date_obj.strftime('%B %d, %Y')
                except:
                    formatted_date = result['date']
                
                with st.container():
                    st.markdown(f"""
                        <div class="article-card">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                                <span class="category-badge">{result['category']}</span>
                                <span class="score-badge">Relevance: {result['score']:.1%}</span>
                            </div>
                            <h3>{result['headline']}</h3>
                            <p style="color: #555; margin: 1rem 0;">{result['short_description']}</p>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="color: #666;"><small>📅 {formatted_date}</small></span>
                                <a href="{result['link']}" target="_blank" class="article-link">
                                    Read full article →
                                </a>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

# Sidebar with statistics
st.sidebar.markdown("""
    <div style="color: white;">
        <h2 style="color: white;">📊 Dataset Statistics</h2>
    </div>
""", unsafe_allow_html=True)

total_docs = len(ir_system.documents)
categories = set(doc['category'] for doc in ir_system.documents.values())

# Display metrics in custom styled cards
st.sidebar.markdown("""
    <div class="metric-card">
        <h4 style="color: white; margin: 0;">Total Articles</h4>
        <h2 style="color: white; margin: 0;">{}</h2>
    </div>
    <div class="metric-card">
        <h4 style="color: white; margin: 0;">Categories</h4>
        <h2 style="color: white; margin: 0;">{}</h2>
    </div>
""".format(total_docs, len(categories)), unsafe_allow_html=True)

# Show categories with counts
st.sidebar.markdown("<h3 style='color: white;'>📑 Category Distribution</h3>", unsafe_allow_html=True)
for category in sorted(categories):
    count = sum(1 for doc in ir_system.documents.values() if doc['category'] == category)
    percentage = (count / total_docs) * 100
    st.sidebar.markdown(f"""
        <div style="color: white; margin-bottom: 0.5rem;">
            • {category}
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 6px; margin-top: 4px;">
                <div style="background: white; width: {percentage}%; height: 100%; border-radius: 10px;"></div>
            </div>
            <small style="color: rgba(255,255,255,0.7);">{count} articles ({percentage:.1f}%)</small>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 1rem; color: #666;">
        <small>Built with Streamlit • Powered by NLTK and scikit-learn</small>
    </div>
""", unsafe_allow_html=True)
