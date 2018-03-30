from flask import Flask, render_template #import moulde Flask
app = Flask(__name__)


@app.route('/')     # vao trang chu, chay ham duoc dinh nghia phia duoi
def index():
    posts =[
            {'title' : 'Thơ con ếch',
            'content': 'Hôm nay trăng lên cao quá \n Anh muốn hôn em vào má',
            'gender': 1,
            'author': 'Tuấn Anh'},
            {'title' : 'Ăn kem',
            'content': 'Ngày ngày ta đứng bên em Ta đứng trước cổng ăn kem Tràng Tiền',
            'gender': 1,
            'author': 'Diễn'},
            {'title' : 'Tao đẹp',
            'content': 'Em không làm thơ được',
            'gender': 0,
            'author': 'Nhi'}
            ]

    return render_template('index.html',posts = posts )

@app.route('/hello')
def hello():
    return 'Hello C4E 16'

@app.route('/say_hi/<name>/<age>')
def say_hi(name,age):
    return 'Hi ' + name + '.You are ' + age + 'years old'

# @app.route('/sum/<x>/<y>')
# def calc(x,y):
#     int_x = int(x)
#     int_y = int(y)
#     # return ('{}'.format(x) + '+' + '{}'.format(y) + '=' + '{}'.format((int_x + int_y)))
#     return str(int_x + int_y)

@app.route('/sum/<int:x>/<int:y>')
def calc(x,y):
    return str(x + y)

if __name__ == '__main__':  # neu chay python app.py truc tiep moi chay ham duoi
  app.run(debug=True)   # khoi dong server, code thay doi tu dong cap nhat moi
