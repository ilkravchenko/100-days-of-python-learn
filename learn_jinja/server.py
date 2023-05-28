from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.today().year
    return render_template('index.html', random_number=random_number, year=current_year)


@app.route('/guess/<name>')
def request_to_api(name):
    agife_url = f'https://api.agify.io?name={name}'
    genderize_url = f'https://api.genderize.io?name={name}'

    response = requests.get(url=agife_url)
    response.raise_for_status()
    data = response.json()
    age = data['age']
    # print(age)

    response = requests.get(url=genderize_url)
    response.raise_for_status()
    data = response.json()
    gender = data['gender']

    return render_template('api_name.html', name=name.capitalize(), gender=gender, years=age)


@app.route('/blog')
def get_blog():
    blog_api = 'https://api.npoint.io/c790b4d5cab58020d391'

    response = requests.get(url=blog_api)
    blogs = response.json()

    return render_template('blog.html', posts=blogs)


if __name__ == '__main__':
    app.run(debug=True)
