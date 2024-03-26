from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Новостной сайт',
        'text': 'Скоро тут будут новости!'
    }
    return render_template(
        'index.html',
        **context
    )


if __name__ == '__main__':
    app.run(debug=True)
