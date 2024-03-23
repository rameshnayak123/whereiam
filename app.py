from flask import Flask,render_template,Response
import os
import sys

# Add the directory containing captureTitle.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'program')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Main')))

from saveTitleContentThumnail import saveTCT
from Magic import magic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# capturing Title,Content and Thumbnail
@app.route('/get_title_content_and_thumbnail', methods=['POST'])
def get_title_content_and_thumbnail():
    return saveTCT()


# checking that magic link is working or not
@app.route('/magic/<string:id>', methods=['GET'])
def get_data_by_id(id):
    response = magic(id)
    data = response.get_json()
    return render_template('template1.html', data=data)
    

@app.route("/client")
def client():
    return render_template('clientSide/clientDashboard.html')  
        

if __name__ == '__main__':
    app.run(debug=True)
