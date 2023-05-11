from datetime import datetime, date, time
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3
db = SQLAlchemy(app)
data = [[1 ,2], [3, 4], [5, 6], [7, 8], [9, 10]]


Class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
db.create_all()

Class NewsForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="message is to be not empty")])


Class FeedbackForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="message is to be not empty")])

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
# проекты:(базы,  парсинг, данных тесты,) слежка за ценами, парсинг афиши, прежде чем задавать вопрос задать его гуглу