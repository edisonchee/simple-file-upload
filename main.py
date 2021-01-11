import socket
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def render():
  return render_template('index.html', ip=socket.gethostbyname(socket.gethostname()))
	
@app.route('/upload', methods = ['POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'

# app.config['UPLOAD_FOLDER'] = 'USE_ABSOLUTE_PATH'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.run(host='0.0.0.0', debug = True)