from flask import Flask
from uuid import UUID
app = Flask(__name__)
@app.route('/')
def home():
    return ('Hello Dear!')

@app.route("/user/<int:id>")
def users(id):
    return f'User ID: {id}'

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

@app.route("/price/<float:amount>")
def price(amount):
    return f'Price: {amount}'

if __name__ == '__main__':
    app.run(debug=True)