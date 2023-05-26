from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_func():
        result = func()
        return f"<b>{result}</b>"

    return wrapper_func


def make_emphasis(func):
    def wrapper_func():
        result = func()
        return f"<em>{result}</em>"

    return wrapper_func


def make_underlined(func):
    def wrapper_func():
        result = func()
        return f"<u>{result}</u>"

    return wrapper_func


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is paragraph</p>' \
           '<img sourse="https://www.thedailyworld.com/wp-content/uploads/2020/05/21591430_web1_KittenRescue-ADW-200520-kitten_2.jpg">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


@app.route('/username/<name>')
def greet(name):
    return f'Hello {name}!'


@app.route('/username/<name>/<int:number>')
def greet_age(name, number):
    return f'Hello {name}! You are {number} years old?'


if __name__ == '__main__':
    app.run(debug=True)
