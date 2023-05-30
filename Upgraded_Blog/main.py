import requests
from post import Post
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    blog_api = 'https://api.npoint.io/8440265fff298c576c0f'

    response = requests.get(url=blog_api)
    blogs = response.json()

    return render_template("index.html", posts=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:num>')
def redirect_to_post(num):
    post = Post(post_id=num)

    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)