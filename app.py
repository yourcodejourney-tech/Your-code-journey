from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/enroll")
def enroll():
    return render_template("enroll.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save data into file
    with open("users.txt", "a") as f:
        f.write(f"Name: {name} | Email: {email} | Time: {time}\n")

    return render_template("thankyou.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
