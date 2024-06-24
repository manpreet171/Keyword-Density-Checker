import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

def plot_wordcloud(keyword_freq):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keyword_freq)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def plot_histogram(keyword_freq, density, top_n=10):
    top_keywords = keyword_freq.most_common(top_n)
    keywords, freqs = zip(*top_keywords)
    colors = ['green' if density[kw] < 3 else 'red' for kw in keywords]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(keywords, freqs, color=colors)
    ax.set_xlabel('Keywords')
    ax.set_ylabel('Frequency')
    ax.set_title('Top Keywords')
    plt.xticks(rotation=45, ha='right')
    
    for bar, kw in zip(bars, keywords):
        height = bar.get_height()
        ax.annotate(f'{density[kw]:.2f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    st.pyplot(fig)
