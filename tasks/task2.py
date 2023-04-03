from flask import Flask

app = Flask(__name__)


@app.route('/<int:a>/<string:operation>/<int:b>')
def get_date_or_time(a, operation, b):
    if operation == '+':
        return f'<h1>{a + b}</h1>'
    elif operation == '-':
        return f'<h1>{a - b}</h1>'
    elif operation == '*':
        return f'<h1>{a * b}</h1>'
    elif operation == ':':
        return f'<h1>{a / b}</h1>' if b != 0 else '<h1>Ошибка</h1>'
    else:
        return '<h1>Простите, но я вас не понимать.</h1>'


@app.route('/')
@app.route('/<path:error1>')
def error(error1=''):
    return f'Неправильный ввод параметров - {error1}'


if __name__ == '__main__':
    app.run(debug=True)
