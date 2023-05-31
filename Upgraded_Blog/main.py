import requests
import smtplib
from post import Post
from datetime import datetime
from flask import Flask, render_template, request

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        MY_EMAIL = "bilbob172839@gmail.com"
        PASSWORD = "bswxpubchiudxhwi"

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        print(name)
        print(email)
        print(phone)
        print(message)

        data = [name, email, phone, message]

        message_to_follower = f'Subject:Success!\n\nHi {name.title()}, it\'s Illia. I have received your message and will reply ASAP.'
        message_to_me = f'Subject:New Email!\n\nMessage - {message}\nFrom - {email}.'
        message_to_me = message_to_me.encode('utf-8')
        message_to_follower = message_to_follower.encode('utf-8')


        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=message_to_follower)

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=message_to_me)

        return render_template('contact.html', data=data)

    return render_template('contact.html')

@app.route('/post/<int:num>')
def redirect_to_post(num):
    post = Post(post_id=num)

    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)