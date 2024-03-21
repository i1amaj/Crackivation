from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

app = Flask(__name__)
db = SQL("sqlite:///project.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def main():
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # naming input variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        image = request.form.get("image")

        if password != confirmation:
            error = "Password doesn't match!"
            return render_template("register.html", error=error)

        elif username:
            result = db.execute("SELECT * FROM users WHERE username = ?", username)
            if len(result) > 0:
                error = "Username taken!"
                return render_template("register.html", error=error)
            else:
                # encrypting the passcode
                hash = generate_password_hash(password)

                # updating users table
                db.execute(
                    "INSERT INTO users (username, hash) VALUES(?,?)", username, hash
                )

                # getting user_id
                user_id_dic = db.execute(
                    "SELECT id FROM users WHERE username = ?", username
                )
                user_id = user_id_dic[0]["id"]

                # creating there data base
                db.execute(
                    "INSERT INTO data (user_id, todo, journal, analysis, crackivation) VALUES(?,?,?,?,?)",
                    user_id,
                    "",
                    "",
                    "",
                    "",
                )
                return redirect("/login")

    error = ""
    return render_template("register.html", error=error)


@app.route("/login", methods=["POST", "GET"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            user = db.execute("SELECT * FROM users WHERE username = ?", username)

            if len(user) != 1 or not check_password_hash(user[0]["hash"], password):
                error = "Invalid username and/or password!"
                return render_template("login.html", error=error)

            session["user_id"] = user[0]["id"]

            return redirect("/todo")

    error = ""
    return render_template("login.html", error=error)


@app.route("/journal", methods=["POST", "GET"])
def journal():
    if request.method == "POST":
        data = request.form.get("data")
        db.execute(
            "UPDATE data SET journal = ? WHERE user_id = ?", data, session["user_id"]
        )

        return render_template("journal.html", data=data)

    else:
        datas = db.execute(
            "SELECT journal FROM data WHERE user_id = ?", session["user_id"]
        )
        data = datas[0]["journal"]
        return render_template("journal.html", data=data)


@app.route("/todo", methods=["POST", "GET"])
def todo():
    if request.method == "POST":
        data = request.form.get("data")
        db.execute(
            "UPDATE data SET todo = ? WHERE user_id = ?", data, session["user_id"]
        )

        return render_template("todo.html", data=data)

    else:
        datas = db.execute(
            "SELECT todo FROM data WHERE user_id = ?", session["user_id"]
        )
        data = datas[0]["todo"]
        return render_template("todo.html", data=data)


@app.route("/crackivation", methods=["POST", "GET"])
def cractivation():
    if request.method == "POST":
        analysis = request.form.get("analysis")
        db.execute(
            "UPDATE data SET analysis = ? WHERE user_id = ?",
            analysis,
            session["user_id"],
        )

        if request.form.get("crackivation") == "":
            crackivation = request.form.get("template")
        else:
            crackivation = request.form.get("crackivation")

        db.execute(
            "UPDATE data SET crackivation = ? WHERE user_id = ?",
            crackivation,
            session["user_id"],
        )

        return render_template(
            "crackivation.html", analysis=analysis, crackivation=crackivation
        )

    else:
        datas = db.execute(
            "SELECT analysis,crackivation FROM data WHERE user_id = ?",
            session["user_id"],
        )
        analysis = datas[0]["analysis"]
        crackivation = datas[0]["crackivation"]

        return render_template(
            "crackivation.html", analysis=analysis, crackivation=crackivation
        )
