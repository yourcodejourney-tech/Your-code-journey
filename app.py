from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    topic = request.form['topic']
    return f"""
    <h2>Thank You {name}!</h2>
    <p>We received your email: {email}</p>
    <p>Your Interest Topic: {topic}</p>
    <a href="/">Go Back</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
