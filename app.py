"""Mans Flask projekts"""

from flask import (
    Flask,
    request,
    render_template
)
from config import Config
import sqlite3
from pprint import pprint

con = sqlite3.connect("db/books.db", check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/sakums", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        pass
    else:
        sql = """
            SELECT 
            Books.book_id,
            Books.author,
            Books.name AS book_name,
            Books.pages,
            Genres.name AS genre_name
            FROM Books
            JOIN Genres ON Genres.genre_id = Books.genre_id;
            """
        res = cur.execute(sql)
        books = res.fetchall()
        pprint(books)
        
        return render_template("books.html", mybooks=books)

@app.route("/pievienot_gramatu", methods = ["GET", "POST"])
def add_book():
    if request.method == "POST":
        author = request.form["book_author"]
        #author = request.form.get("book_author", None)
        name = request.form["book_name"]
        pages = request.form["book_pages"]
        
    else:
        sql = """
            SELECT *
            FROM genres;"""
        res = cur.execute(sql)
        genres = res.fetchall()
        pprint(genres)
        return render_template("add_book.html", genres=genres)

if app.config["FLASK_ENV"] == "development":
    if __name__ == "__main__":
        app.run(debug=True)