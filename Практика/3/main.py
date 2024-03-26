from flask import Flask, render_template

app = Flask(__name__)


def load_tags():
    # напишите функцию получения тегов из файла и создания словаря tags_dict
    with open('tags.txt') as f:
        pass


@app.route('/')
def tag_cloud():
    tags_dict = load_tags()
    return render_template('index.html', tags=tags_dict)


if __name__ == '__main__':
    app.run(debug=True)
