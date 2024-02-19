from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "<b>Миссия Колонизация Марса</b>"


@app.route('/index')
def index():
    return "<b>И на Марсе будут яблони цвести!</b>"


@app.route('/promotion')
def promo():
    return "<b>Человечество вырастает из детства.<br> <br> Человечеству мала одна планета. <br><br> Мы сделаем обитаемыми безжизненные пока планеты.<br><br> И начнем с Марса! <br><br> Присоединяйся!</b>"


@app.route('/image_mars')
def mars():
    return "<h1>Жди нас, Марс!</h1><br><img src='/static/istockphoto-1300652810-612x612.jpg'></img>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
