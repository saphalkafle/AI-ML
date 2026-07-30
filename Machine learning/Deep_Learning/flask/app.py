# for jinja inheritance
from flask import Flask,render_template,jsonify,url_for

inherit = Flask(__name__)

@inherit.route("/inheritance")
def inheritance():
    return render_template("index.html")





if __name__ == "__main__":
    inherit.run(debug = True)