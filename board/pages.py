from flask import Blueprint, render_template, request, redirect, url_for
from board.database import get_db   # sesuai dengan database.py

bp = Blueprint("pages", __name__, url_prefix="/")

# Halaman utama
@bp.route("/")
def home():
    return render_template("pages/home.html")

# Halaman about
@bp.route("/about")
def about():
    return render_template("pages/about.html")

# Daftar postingan
@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT id, title, body FROM posts ORDER BY id DESC"
    ).fetchall()
    return render_template("pages/posts.html", posts=posts)

# Membuat postingan baru
@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]   # konsisten dengan schema.sql (bukan content)

        db = get_db()
        db.execute(
            "INSERT INTO posts (title, body) VALUES (?, ?)",
            (title, body),
        )
        db.commit()

        return redirect(url_for("pages.posts"))

    return render_template("pages/create.html")
