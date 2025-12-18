from flask import Flask, render_template, request, redirect, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "super_secret_key"

def get_db():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = hash_password(request.form["password"])

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            return redirect("/notes")

    return render_template("login.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    password = hash_password(request.form["password"])

    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )
        conn.commit()
    except:
        pass
    conn.close()
    return redirect("/")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if "user_id" not in session:
        return redirect("/")

    conn = get_db()

    if request.method == "POST":
        note = request.form["note"]
        if note.strip():
            conn.execute(
                "INSERT INTO notes (user_id, content) VALUES (?, ?)",
                (session["user_id"], note)
            )
            conn.commit()

    notes = conn.execute(
        "SELECT * FROM notes WHERE user_id=?",
        (session["user_id"],)
    ).fetchall()

    conn.close()
    return render_template("notes.html", notes=notes, name=session["user_name"])

@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        return redirect("/")

    conn = get_db()
    conn.execute(
        "DELETE FROM notes WHERE id=? AND user_id=?",
        (id, session["user_id"])
    )
    conn.commit()
    conn.close()
    return redirect("/notes")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
