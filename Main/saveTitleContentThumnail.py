import os,json,sys,string
from flask import request,jsonify
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'program')))

from randomCode import generate_random_code
from captureTitle import extract_title
from extractContent import extract_content
from extractThumbnail import extract_thumbnail
from saveImage import save_image
from saveJson import save_json


def saveTCT():
    domain_name = "https://5000-rameshnayak123-whereiam-fqs89wrys0s.ws-us110.gitpod.io"
    url = request.json['url']
    cardName = request.json['cardName']
    random_code = generate_random_code(14)
    title = extract_title(url)
    content = extract_content(url)
    thumbnail = extract_thumbnail(url)
    img_name = save_image(thumbnail)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'id': random_code,
        'cardName' : cardName,
        'title': title,
        'content': content,
        'image_path': f'/static/images/{img_name}',
        'url':url,
        'date_time': current_time,
        'magic_url': f'{domain_name}/magic/{random_code}'
    }
    json_name = save_json(data)
    
    # Return the saved JSON data
    return jsonify(data)