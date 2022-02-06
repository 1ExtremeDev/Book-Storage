from flask import Flask, send_file; import os
app = Flask(__name__)

@app.route('/')
def index():
    _dir = [os.path.join('book/', o) for o in os.listdir('book/') if os.path.isdir(os.path.join('book/',o))]; text = ""
    for each in _dir: each = each.split('/')[1]; text+=f'<a href="/{each}">{each}</a><br >'
    return text

@app.route('/<name>')
def folder(name):
    if os.path.exists(f'book/{name}'):
        filenames = next(os.walk(f'book/{name}'), (None, None, []))[2]; text = ""
        for each in filenames: z=each.split('.')[0]; text+=f'<a href="/{name}/{each}">{z}</a><br >'
        return text
    else: return '<h1>Folder does not exist</h1>'

@app.route('/<name>/<book>')
def book(name, book):
    if os.path.exists(f'book/{name}/{book}'): return send_file(f'book/{name}/{book}', as_attachment=True)
    else: return '<h1>File does not exist</h1>'

if __name__ == "__main__": app.run(debug=True)