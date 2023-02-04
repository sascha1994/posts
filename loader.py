from flask import Blueprint, render_template, request
from functions import add_from_json

loader_blueprint = Blueprint('loader_blueprint', __name__)

@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route("/upload", methods=["POST"])
def page_post_upload():
    picture = request.files.get('picture')
    filename = picture.filename
    picture.save(f'./uploads/images/{filename}')
    image = f'./uploads/images/{filename}'
    content = request.form['content']
    add_from_json(image, content)
    try:
        return render_template('post_uploaded.html', content = content, image = image)
    except:
        return 'ошибка загрузки'