import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text, n_gram=1):
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\W+', ' ', text)
    vectorizer = CountVectorizer(ngram_range=(n_gram, n_gram), stop_words='english')
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    counts = X.toarray().sum(axis=0)
    return list(zip(keywords, counts))

def keyword_density(keywords, total_words):
    keyword_freq = Counter(dict(keywords))
    density = {kw: (freq / total_words) * 100 for kw, freq in keyword_freq.items()}
    return keyword_freq, density

def keyword_meta_analysis(soup, keywords, density):
    meta_title = soup.find('title').get_text().lower() if soup.find('title') else ""
    meta_desc = soup.find('meta', attrs={'name': 'description'})['content'].lower() if soup.find('meta', attrs={'name': 'description'}) else ""
    
    analysis = []
    for kw, freq in keywords:
        in_title = 'yes' if kw in meta_title else 'no'
        in_desc = 'yes' if kw in meta_desc else 'no'
        in_headings = 'yes' if any(kw in heading.get_text().lower() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])) else 'no'
        analysis.append([kw, freq, density[kw], in_title, in_desc, in_headings])
    
    return analysis
