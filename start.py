import uuid

from flask import Flask


app = Flask(__name__)
x = uuid.uuid4()
print(x)


@app.route('/news_detail/<float:id>')
def new_detail1(id):
    return f'Новость {id}'


@app.get('/news_detail/<uuid:number>')
def  view_uuid(number):
    return f'Приведен {number} номер'


@app.route('/news_detail/<string:name>')
def new_detail(name):
    return f'Категория {name}'


@app.get('/news_detail/<path:new_path>')
def new_pathed(new_path):
    return f'Путь: {new_path}'


if __name__ == '__main__':
    app.run(debug=True)