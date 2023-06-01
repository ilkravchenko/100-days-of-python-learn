from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="uh327yalkjd9723LASF78lkasd",
    WTF_CSRF_SECRET_KEY="kljh798123hlasd9812kasd98k"
))
Bootstrap(app)


class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired("Please enter your email.")])
    password = PasswordField(label='Password', validators=[DataRequired("Please enter your password."), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
