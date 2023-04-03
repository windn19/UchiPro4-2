from flask import Flask

app = Flask(__name__)


@app.route('/total/<int:a>/<int:b>')
def total(a, b):
    return f'Сумма: {a + b}'


if __name__ == '__main__':
    app.run(debug=True)
