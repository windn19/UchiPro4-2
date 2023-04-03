from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Главная страница'


@app.route('/news')
def new_detail1():
    return 'Новости'


@app.route('/news_detail/<int:id>')
def new_detail(id):
    return f'Новость {id}'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('new_detail1'))
    print(url_for('new_detail', id=1))

# if __name__ == '__main__':
#     app.run(debug=True)