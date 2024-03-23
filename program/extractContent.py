import requests
from bs4 import BeautifulSoup


def extract_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ''.join([p.get_text() for p in paragraphs[:1]])
        return content
    except Exception as e:
        return str(e)