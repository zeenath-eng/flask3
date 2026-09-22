from flask import Flask
from uuid import UUID
app = Flask(__name__)
@app.route('/')
def home():
    return ('Hello Dear!')

@app.route("/user/<int:id>")
def users(id):
    return f'User ID: {id}'

@app.route("/files/<path:fill
@app.route("/price/<float:amount>")
def price(amount):
    return f'Price: {amount}'

if __name__ == '__main__':
    app.run(debug=True)