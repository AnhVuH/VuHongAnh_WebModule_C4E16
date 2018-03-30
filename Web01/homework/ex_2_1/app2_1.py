from flask import Flask, render_template, request, redirect,url_for
from pymongo import MongoClient

uri = 'mongodb://admin:123456@ds117489.mlab.com:17489/aboco1'
client = MongoClient(uri)
db = client.get_default_database()

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'

@app.route('/', methods =['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('get_profile',username = request.form['username']))
    else:
        return render_template('index.html')

@app.route('/users/<username>')
def get_profile(username):
    return render_template('user_profile.html',user=db.users.find_one({'username': username}))


if __name__ == '__main__':
    app.run(debug=1)
