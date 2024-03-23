import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def extract_thumbnail(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        thumbnail = soup.find('meta', property='og:image')['content']
        return thumbnail
    except Exception as e:
        return str(e)