from flask import Flask, request, jsonify,render_template
from bs4 import BeautifulSoup
import requests

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

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_title', methods=['POST'])
def get_title():
    url = request.json['url']
    title = extract_title(url)
    return jsonify({'title': title})

@app.route('/get_content', methods=['POST'])
def get_content():
    url = request.json['url']
    content = extract_content(url)
    return jsonify({'content': content})

@app.route('/get_thumbnail', methods=['POST'])
def get_thumbnail():
    url = request.json['url']
    thumbnail = extract_thumbnail(url)
    return jsonify({'thumbnail': thumbnail})

if __name__ == '__main__':
    app.run(debug=True)
