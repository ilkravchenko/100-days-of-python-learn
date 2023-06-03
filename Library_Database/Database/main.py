from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f'{self.title} - {self.author} - {self.rating}'

app.app_context().push()
db.create_all()
potter = Book(title='Harry Pottr', author='J. K. Rowlin', rating=9.1)
db.session.add(potter)
db.session.commit()


all_books = db.session.query(Book).all()
book = Book.query.filter_by(title="Harry Potter").first()

book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()


book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()


book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()















# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
#
# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# #cursor.execute("INSERT INTO books VALUES(1, 'Harry Poter', 'J. K. Rowling', '9.3')")
# db.commit()