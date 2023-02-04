import json


def load_from_json():
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def get_posts_by_word(word):
    print(word)
    posts = []
    for content in load_from_json():
        post = content['content'].split()
        post = [x.lower() for x in post]
        for i in range(len(post)):
            f = filter(str.isalpha, post[i])
            post[i] = "".join(f)
        if word in post:
            posts.append(content)
    return posts


def add_from_json(pic, content):
    data = {'pic': pic, 'content': content}
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        posts.append(data)

    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)


