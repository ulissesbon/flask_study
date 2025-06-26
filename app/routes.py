from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ulisses'}
    posts = [
        {
            'author': {'username': 'Pedro'},
            'body': 'Comecei a usar o Vim!'
        },
        {
            'author': {'username': 'Marcelo'},
            'body': 'Odeio o Vim!'
        }
    ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)