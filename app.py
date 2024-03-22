from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import os
import json
from datetime import datetime

app = Flask(__name__)

def extract_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        return title
    except Exception as e:
        return str(e)

def extract_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = '\n'.join([p.get_text() for p in paragraphs[:1]])
        return content
    except Exception as e:
        return str(e)

def extract_thumbnail(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        thumbnail = soup.find('meta', property='og:image')['content']
        return thumbnail
    except Exception as e:
        return str(e)

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

def save_json(data):
    try:
        json_name = datetime.now().strftime("%Y%m%d%H%M%S") + '.json'
        json_path = os.path.join('static/json', json_name)
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return json_name
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_title_content_and_thumbnail', methods=['POST'])
def get_title_content_and_thumbnail():
    url = request.json['url']
    title = extract_title(url)
    content = extract_content(url)
    thumbnail = extract_thumbnail(url)
    img_name = save_image(thumbnail)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'title': title,
        'content': content,
        'image_path': f'/static/images/{img_name}',
        'date_time': current_time
    }
    json_name = save_json(data)
    
    # Read the JSON file and return its contents
    with open(os.path.join('static/json', json_name), 'r') as json_file:
        json_data = json.load(json_file)
    
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
