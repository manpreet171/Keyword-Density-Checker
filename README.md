# Keyword Density Checker

This project is a Streamlit application that analyzes the keyword density of a given website URL. It uses NLP techniques to extract keywords and provides visualizations such as word clouds and histograms, making it useful for SEO experts.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Logic and Workflow](#logic-and-workflow)
- [Libraries Used](#libraries-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Keyword-Density-Checker.git
    cd Keyword-Density-Checker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure spaCy model is downloaded:
    ```sh
    python -m spacy download en_core_web_sm
    ```

## Usage

To run the application, use the following command:
```sh
streamlit run app.py



**Project Structure**


- app.py: The main Streamlit application file.
- utils/: Contains utility modules for text extraction, keyword analysis, and visualization.
- text_extraction.py: Functions for extracting text from HTML.
- keyword_analysis.py: Functions for extracting and analyzing keywords.
- visualization.py: Functions for creating visualizations (word clouds and histograms).


**Logic and Workflow**


- Fetch Page Content: The app fetches the HTML content of the provided URL using the requests library.
- Extract Text: It extracts visible text, including optional titles and ALT attributes, using BeautifulSoup.
- Keyword Extraction: Using CountVectorizer from sklearn, the app extracts keywords and their frequencies. It supports one-word to four-word phrases.
- Keyword Density Calculation: Calculates the density of each keyword as a percentage of total words.
- Meta Analysis: Checks if keywords appear in meta titles, descriptions, and heading tags.
- Visualizations: Creates a word cloud and a histogram of the top keywords, color-coded based on density.


**Libraries Used**

- Streamlit: For building the web application.
- requests: For making HTTP requests to fetch webpage content.
- BeautifulSoup4: For parsing HTML content.
- spaCy: For advanced NLP processing.
- scikit-learn: For keyword extraction and vectorization.
- Matplotlib: For creating visualizations.
- WordCloud: For generating word clouds.

