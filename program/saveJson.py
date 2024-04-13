import os
import json


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

def save_indexdata(indexdata):
    json_file_path = 'static/json/unregdata.json'
    existing_data = []
    try:
        # Read existing JSON data
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                existing_data = json.load(json_file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")

    # Append new data to existing JSON data
    existing_data.append(indexdata)

    try:
        # Write updated JSON data back to the file
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)
    except Exception as e:
        print(f"Error writing JSON file: {e}")

    return json_file_path