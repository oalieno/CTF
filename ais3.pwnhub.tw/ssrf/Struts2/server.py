from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    print request.headers
    return "hello orange XD\n"

@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files',path)

app.run(host = "0.0.0.0")
