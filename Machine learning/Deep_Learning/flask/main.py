from flask import Flask,render_template

app = Flask(__name__,static_folder = "assets",static_url_path = "/assets_new")

@app.route("/")

def introduction():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
