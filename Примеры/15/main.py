from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Новостной сайт',
        text='Скоро тут будут новости!'
    )


if __name__ == '__main__':
    app.run(debug=True)
