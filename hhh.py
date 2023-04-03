from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Моя страница</title>
    </head>
    <body>
        <h1>Привет, мир</h1>
        <p>Я создал эту страницу с помощью Flask</p>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)
