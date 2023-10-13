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
            Books.name,
            Books.pages,
            Genres.name
            FROM Books
            JOIN Genres ON Genres.genre_id = Books.genre_id;
            """
        res = cur.execute(sql)
        books = res.fetchall()
        pprint(books)
        
        return render_template("books.html", mybooks=books)

if app.config["FLASK_ENV"] == "development":
    if __name__ == "__main__":
        app.run(debug=True)