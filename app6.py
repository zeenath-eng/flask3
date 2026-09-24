from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    courses=[
        "python",
        "Flask",
        "Django",
        "SQLAlchemy",
        "Flask-SQLAlchemy",
    ]
    student= {
         "name":"zeenath",
         "course":"Flask",
         "city":"Hyderabad"
    }
    return render_template('index3.html', courses=courses, student=student)

if __name__ == '__main__':
    app.run(debug=True)
