from flask import Flask,render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)


conn = sqlite3.connect("database.sqlite")
sql = "CREATE TABLE IF NOT EXISTS Student(id INTEGER PRIMARY KEY, name TEXT, class TEXT, gender TEXT)"

conn.execute(sql)

@app.route("/")
def index():
    return "Hello World"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/home/<name>", methods=["GET","POST"])
def user_home(name):
    conn = sqlite3.connect("database.sqlite")
    if request.method == "POST":
        form = request.form
        sql = f"INSERT INTO Student(id,name,class,gender) VALUES({1},{form['Name']},{form['Class']},{form['Gender']})"
        cur = conn.cursor()
        cur.execute("INSERT INTO Student(name,class,gender) VALUES (?, ?, ?)",(form['Name'],form['Class'],form['Gender']))
        conn.commit()
        conn.close()
        return redirect(url_for('user'))
    return render_template("user.html")


@app.route("/user")
def user():
    conn = sqlite3.connect("database.sqlite")
    posts = conn.execute("SELECT * FROM Student").fetchall() 
    conn.close()
    return render_template("users.html",posts=posts)


if __name__ == "__main__":
    app.run(debug=True)