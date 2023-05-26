import random
from flask import Flask

app = Flask(__name__)

RANDOM_NUMBER = random.randint(0, 9)

@app.route('/')
def guess():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Correct.gif'>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/<int:number>')
def guessed_random(number):
    if number == RANDOM_NUMBER:
        return '<h1 style="color:purple">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct.gif">'
    elif number > RANDOM_NUMBER:
        return '<h1 style="color:green">To high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="High.gif">'
    else:
        return '<h1 style="color:green">To low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Low.gif">'

if __name__ == '__main__':
    app.run(debug=True)
