from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    is_logged_in = True
    #is_logged_in = False
    marks = 98
    return render_template('index2.html', is_logged_in=is_logged_in, marks=marks)

if __name__ == '__main__':
    app.run(debug=True)
