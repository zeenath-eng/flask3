from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def home():
    name="zeenath"
    course="Flask"
    city="hyderabad"
    return render_template("index.html",
                           name=name,
                           course=course,
                           city=city)

if __name__ == '__main__':
    app.run(debug=True)