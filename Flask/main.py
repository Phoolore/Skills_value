from datetime import datetime, date, time

from flask import Flask, render_template


app = Flask(__name__)
data = [[1 ,2], [3, 4], [5, 6], [7, 8], [9, 10]]
@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    return res


@app.route("/")
def index():
    return render_template('index.html', news = data)


@app.route("/news_detail/<int:id>")
def news_detail(id):
    return render_template('news_details.html', id = id, new = data[id % 6] )
    

def fib(n):
    x1 = 1
    x2 = 1
    yield x1
    yield x2
    for i in range(n):
        x1, x2 = x2 , x1 + x2
        yield x2
        
        
@app.route('/details/<int:id>')
def details(id):
    return f'Новость №{id}'


@app.route("/fib/<int:a>")
def fib_page(a):
    return render_template("fib_page.html", data = [str(i) for i in fib(a)], index = a)


@app.route('/total/<int:a>/<int:b>')
def addition(a, b):
    return str(a + b)


@app.route('/date')
def date_page():
    return datetime.now().strftime("%Y-%m-%d")


@app.route('/time')
def time_page():
    return datetime.now().strftime("%H:%M:%S")


if __name__ == '__main__':
    app.run()
