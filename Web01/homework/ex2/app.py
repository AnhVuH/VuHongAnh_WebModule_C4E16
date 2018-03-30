from flask import Flask, render_template
users = { 'quy' :{
			        'name' : 'Dinh Cong Quy',
                    'gender': 'Male',
			        'age' : 20,
                    'hobbies':'......'
                  },
           'tuananh' : {
			            'name' : 'Huynh Tuan Anh',
                        'gender': 'Male',
			            'age' : 22,
                        'hobbies':'......'
                        },
           'honganh':{
			            'name' : 'Vu Hong Anh',
                        'gender': 'Female',
			            'age' : 29,
                        'hobbies':'Film Photography, Bicyling, Martial Art, Reading book'
                        },

        }
app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'

@app.route('/users/<username>')
def get_profile(username):
    if username in users:
        username = users[username]
    else:
        username = None
    return render_template('user_profile.html',username=username)


if __name__ == '__main__':
    app.run(debug=1)
