import logging
from flask import Blueprint, render_template, request
import functions

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route("/list")
def page_tag():
    items = functions.load_from_json()
    return render_template('post_list.html', items=items)


@main_blueprint.route('/search')
def search_page():
    s = request.args['s']
    logging.info('Выполняется поиск')
    items = functions.get_posts_by_word(s)
    return render_template('post_list.html', items=items, word=s)
