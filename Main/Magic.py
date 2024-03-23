from flask import jsonify
import os,json,sys

def magic(id):
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
            return jsonify({'error': 'Entry not found May be Magic link expired create new'})
    except Exception as e:
        return jsonify({'error': f'Error: {e}'})