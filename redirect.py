from flask import Flask


app = Flask(__name__)


@app.route('/category/')
def category():
    return 'Категории новостей'


@app.route('/news')
def new_detail():
    return 'Новости'


if __name__ == '__main__':
    app.run(debug=True)