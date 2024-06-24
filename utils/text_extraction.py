import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def extract_text(soup, include_titles=True, include_alt_titles=True):
    texts = []
    if include_titles:
        for title in soup.find_all(['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            texts.append(title.get_text())

    if include_alt_titles:
        for img in soup.find_all('img'):
            alt_text = img.get('alt')
            if alt_text:
                texts.append(alt_text)
    
    for p in soup.find_all('p'):
        texts.append(p.get_text())
    
    return " ".join(texts)
