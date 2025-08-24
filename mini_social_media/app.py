from flask import Flask, render_template, request, redirect, url_for
import os
from caption_generator import generate_caption

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        file = request.files['media']
        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            caption = generate_caption(path)
            return render_template('post.html', media=file.filename, caption=caption)
    return render_template('post.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
