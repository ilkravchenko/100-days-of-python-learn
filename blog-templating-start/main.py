from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_api = 'https://api.npoint.io/c790b4d5cab58020d391'

    response = requests.get(url=blog_api)
    blogs = response.json()

    return render_template("index.html", posts=blogs)

@app.route('/post/<int:num>')
def redirect_to_post(num):
    post = Post(post_id=num)

    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)
