from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

if __name__ == '__main__':
    app.run(debug=True)