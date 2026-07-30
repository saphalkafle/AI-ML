from flask import Flask,render_template, url_for ,request,jsonify

app = Flask(__name__,static_folder = "assets",static_url_path = "/assets_new")

@app.route("/")
def introduction():
    name = request.args.get("name",default = "anonymous")
    subject = request.args.get("subject")
    print(name)
    print(subject)
    return render_template("index.html",name=name,subject=subject)


@app.route("/login", methods =["GET","POST"])
def login():
    if request.method == "POST":

        #to individually access both
        name = request.form["username"]
        password = request.form["password"]
        friends = ["ram","hari","sita"]
        header = "<header>My personal website</header>"
        #send ot to database and verify
        return render_template("welcome.html",name=name , password=password,friends=friends,header = header)
    else:
        return render_template("login.html")
        
@app.route("/aj")
def api_json():
    data = {
        "message":"Welcome to the platform"
    }

    return jsonify(data) , 200


if __name__ == "__main__":
    app.run(debug=True)
