from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello Flask!'

@app.route("/about")
def about():
    return 'welcome to About page'

@app.route("/contact")
def contact():
    return 'this is a contact page'

@app.route("/users")
def users():
    return 'this is a users page'
@app.route('/user/<name>')
def user(name):
    return f'Hello {name}!'

@app.route('/student/<name>/<course>')
def student(name,course):
    return f'{name} is learning {course}'

if __name__ == '__main__':
    app.run(debug=True)
