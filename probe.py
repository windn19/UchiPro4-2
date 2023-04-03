from flask import Flask


app = Flask(__name__)


@app.route('/route/', defaults={'id': 1})
@app.route('/route/<int:id>')
def region(id):
    return f'<h1>Region {id}</h1>'
