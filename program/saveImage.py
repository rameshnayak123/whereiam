from bs4 import BeautifulSoup
import requests
import os,string
from datetime import datetime

def save_image(url):
    try:
        response = requests.get(url)
        img_data = response.content
        img_name = datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        img_path = os.path.join('static/images', img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        return img_name
    except Exception as e:
        return str(e)

def save_imageindex(url):
    try:
        response = requests.get(url)
        img_data = response.content
        img_name = datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        img_path = os.path.join('static/indeximages', img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        return img_name
    except Exception as e:
        return str(e)