
import pandas as pd
import streamlit as st
from utils.text_extraction import fetch_page_content, extract_text
from utils.keyword_analysis import extract_keywords, keyword_density, keyword_meta_analysis
from utils.visualization import plot_wordcloud, plot_histogram

# Streamlit app layout
st.title('Keyword Density Checker')
st.markdown("This app analyzes the keyword density of a given website URL.")

url = st.text_input('Website URL')
include_titles = st.checkbox('Include Titles', value=True)
include_alt_titles = st.checkbox('Include ALT Titles', value=True)
keyword_type = st.selectbox('Select Keyword Type', ['One word', 'Two words', 'Three words', 'Four words'])

if st.button('Analyze'):
    with st.spinner('Fetching and analyzing content...'):
        soup = fetch_page_content(url)
        text = extract_text(soup, include_titles, include_alt_titles)
        total_words = len(text.split())

        if keyword_type == 'One word':
            keywords = extract_keywords(text, 1)
        elif keyword_type == 'Two words':
            keywords = extract_keywords(text, 2)
        elif keyword_type == 'Three words':
            keywords = extract_keywords(text, 3)
        elif keyword_type == 'Four words':
            keywords = extract_keywords(text, 4)
        
        keyword_freq, density = keyword_density(keywords, total_words)
        keyword_analysis = keyword_meta_analysis(soup, keywords, density)

        st.write(f"Total Keywords: {total_words}")
        
        st.subheader('Word Density Word Cloud')
        plot_wordcloud(keyword_freq)
        
        st.subheader('Top 10 Keywords Histogram')
        plot_histogram(keyword_freq, density)
        
        st.subheader('Top Keywords Analysis')
        columns = ['Keyword', 'Frequency', 'Density (%)', 'In Title', 'In Description', 'In Headings']
        df = pd.DataFrame(keyword_analysis, columns=columns)
        st.dataframe(df)
