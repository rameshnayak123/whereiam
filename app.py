from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import os
import json
import random
import string
from datetime import datetime

app = Flask(__name__)

def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

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
    json_file_path = 'static/json/magic.json'
    existing_data = []

    try:
        # Read existing JSON data
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                existing_data = json.load(json_file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")

    # Append new data to existing JSON data
    existing_data.append(data)

    try:
        # Write updated JSON data back to the file
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)
    except Exception as e:
        print(f"Error writing JSON file: {e}")

    return json_file_path

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_title_content_and_thumbnail', methods=['POST'])
def get_title_content_and_thumbnail():
    url = request.json['url']
    random_code = generate_random_code(8)
    title = extract_title(url)
    content = extract_content(url)
    thumbnail = extract_thumbnail(url)
    img_name = save_image(thumbnail)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'id': random_code,
        'title': title,
        'content': content,
        'image_path': f'/static/images/{img_name}',
        'date_time': current_time,
        'url': f'https://5000-rameshnayak123-whereiam-fqs89wrys0s.ws-us110.gitpod.io/magic/{random_code}'
    }
    json_name = save_json(data)
    
    # Return the saved JSON data
    return jsonify(data)


## checking that magic link is working or not

@app.route('/magic/<string:id>', methods=['GET'])
def get_data_by_id(id):
    json_file_path = 'static/json/magic.json'
    
    try:
        # Read the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Search for the entry with the given ID
        entry = next((item for item in data if item['id'] == id), None)
        
        if entry:
            return jsonify(entry)
        else:
            return jsonify({'error': 'Entry not found'})
    except Exception as e:
        return jsonify({'error': f'Error: {e}'})


if __name__ == '__main__':
    app.run(debug=True)
