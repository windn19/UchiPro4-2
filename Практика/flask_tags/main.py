from flask import Flask, render_template

app = Flask(__name__)


def load_tags():
    with open('tags.txt') as f:
        tags = f.read().strip().split(' ')
        tags_dict = {}
        for tag in tags:
            if tag not in tags_dict:
                tags_dict[tag] = 0
            else:
                tags_dict[tag] += 1
    return tags_dict


@app.route('/')
def tag_cloud():
    tags_dict = load_tags()
    return render_template('index.html', tags=tags_dict)


if __name__ == '__main__':
    app.run(debug=True)
