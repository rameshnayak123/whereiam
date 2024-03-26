import requests
from bs4 import BeautifulSoup
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt')
import re

def extract_content(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text from HTML elements
            content_text = ' '.join([element.get_text() for element in soup.find_all(['p', 'b', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])

            # Remove sentences containing date and time formats
            content_text = re.sub(r'\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|january|february|march|april|may|june|july|august|september|october|november|december|\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|\d{1,2}[./-]\d{4},?|\d{1,2}:\d{2}(?:\s?[AP]M)?(?:\s?IST)?)\b', '', content_text, flags=re.IGNORECASE)

            # Use sumy library for text summarization
            parser = HtmlParser.from_string(content_text, url, Tokenizer("english"))
            summarizer = LsaSummarizer()
            summary = summarizer(parser.document, sentences_count=5)  # Generate a summary with 5 sentences

            # Combine summary sentences into a single string
            summary_text = ' '.join([str(sentence) for sentence in summary])

            return summary_text
        else:
            return f"Failed to fetch content from {url}. Status code: {response.status_code}"
    except Exception as e:
        return str(e)

