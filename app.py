"""Mans Flask projekts"""

from flask import (
    Flask,
    request,
    render_template,
    redirect,
    flash
)
from config import Config
import sqlite3
from pprint import pprint
from uuid import uuid4

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

        # atlasa reitingus
        sql = """
            SELECT book_id, SUM(score), COUNT(rating_id)
            FROM ratings
            GROUP BY book_id;"""
        res = cur.execute(sql)
        ratings = res.fetchall()
        """ for rating in ratings:
            print(
                rating["book_id"], 
                rating["SUM(score)"],
                rating["COUNT(rating_id)"]) """
        
        return render_template(
            "books.html", 
            mybooks=books,
            ratings_by_books=ratings)

@app.route("/pievienot_gramatu", methods = ["GET", "POST"])
def add_book():
    if request.method == "POST":
        author = request.form["book_author"]
        #author = request.form.get("book_author", None)
        name = request.form["book_name"]
        pages = request.form["book_pages"]
        genre = request.form["book_genre"]

        sql = """INSERT
                INTO Books
                (book_id,
                author,
                name,
                pages,
                genre_id)
                VALUES 
                (?, ?, ?, ?, ?);"""
        
        cur.execute(sql,
                (str(uuid4()),
                 author,
                 name,
                 int(pages),
                 genre
                ))
        con.commit()
        flash("Ieraksts pievienots!")
        return redirect("/")
    else:
        sql = """
            SELECT *
            FROM genres;"""
        res = cur.execute(sql)
        genres = res.fetchall()
        
        return render_template("add_book.html", genres=genres)

@app.route("/pievienot_zanru", methods = ["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre_name = request.form.get("genre_name")

        sql = """INSERT INTO Genres 
                    (
                    genre_id,
                    name)
                    VALUES
                    (?, ?);"""
        cur.execute(sql,
                    (str(uuid4()),
                    genre_name)
                    )
        con.commit()

        flash("Žanrs pievienots!")
        return redirect("/")
    else:
        return render_template("add_genre.html")

@app.route("/set_rating")
def set_rating():
    book_id = request.args.get("book_id")
    value = request.args.get("value")
    print(book_id, value)

    sql = """INSERT INTO Ratings (
    rating_id,
    book_id,
    score)
    VALUES (
    ?, ?, ?
    );"""
    cur.execute(sql, (
        str(uuid4()),
        book_id,
        value
    ))
    con.commit()
    flash("Reitings pievienots!")
    return redirect("/sakums")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        pass1 = request.form.get("password1")
        pass2 = request.form.get("password2")
        role = request.form.get("role")

        # pārbauda, vai paroles sakrīt
        if not pass1 == pass2:
            flash("Paroles nesakrīt! Mēģini vēlreiz!")
            return redirect("/register")
        
        sql = """
        SELECT COUNT(username) 
        FROM Users 
        WHERE username = ?;
        """
        res = cur.execute(sql, (username, ))
        existing_users = res.fetchall()

        for record in existing_users:
            for field in record:
                print(field)

        # pārbauda, vai l-vārds eksistē
        if existing_users[0]["COUNT(username)"] != 0:
            flash("Šāds lietotājs jau eksistē! Mēģini vēlreiz!")
            return redirect("/register")
        
        sql = """
        INSERT INTO Users
        (user_id, username, password, role)
        VALUES (
        ?, ?, ?, ?
        );"""

        try:
            cur.execute(sql, (
                str(uuid4()),
                username,
                pass1,
                role
            ))

            con.commit()
            return redirect("/login")
        except:
            flash("Datu bāzes kļūda!")
            return redirect("/register")

    else:
        return render_template("register.html")

if app.config["FLASK_ENV"] == "development":
    if __name__ == "__main__":
        app.run(debug=True)