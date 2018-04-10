from flask import Flask, render_template, request, redirect,url_for, session
from models.classes import Service, User, Order
from datetime import datetime
from gmail import GMail, Message
import mlab
import re

mlab.connect()

app = Flask(__name__)
app.secret_key = 'a-useless-key'

@app.route('/')
def index():
    all_services = Service.objects()
    return render_template('index.html',all_services = all_services)

@app.route('/search/<int:gender_i>')
def search_gender(gender_i):
    services = Service.objects(gender = gender_i)
    return render_template('services_gender.html', services_o = services)

@app.route('/detail/<id_to_find>')
def show_detail(id_to_find):
    if "loged-in" in session:
        service = Service.objects.with_id(id_to_find)
        return render_template('detail.html',service = service)
    else:
        return redirect('login')

@app.route('/admin')
def admin():
    if "loged-in" in session:
        if (User.objects.with_id(session['user_id'])).username == 'admin':  # admin - admin
            all_services = Service.objects()
            return render_template('admin.html', all_services = all_services)
        else:
            return render_template('error.html',error_code = "error_admin_request")
    else:
        return redirect('login')

@app.route('/delete/<id_to_del>')
def delete(id_to_del):
    service = Service.objects.with_id(id_to_del)
    if service == None:
        return "Not found"
    else:
        service.delete()
    return redirect(url_for('admin'))

@app.route('/new_service', methods= ['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template("new-service.html")
    elif request.method=="POST":
        form = request.form
        name = form['name']
        yob = int(form['yob'])
        phone = form['phone number']
        gender = int(form['gender'])
        image = "http://via.placeholder.com/300x200"

        new_service = Service(name = name, yob = yob, phone = phone, gender = gender, image = image)
        new_service.save()
        return redirect(url_for('admin'))


@app.route('/update-service/<id_to_update>', methods =["GET", "POST"])
def update_service(id_to_update):
    service = Service.objects.with_id(id_to_update)
    if service == None:
        return "Not found"
    else:
        if request.method == "GET":
            return render_template('update-service.html',service = service)
        elif request.method =="POST":
            form = request.form
            name = form['name']
            yob = int(form['yob'])
            gender = int(form['gender'])
            height = int(form['height'])
            phone = form['phone']
            address = form['address']
            if form['status'] == "1":
                status = True
            else :
                status = False
            image = form['image']
            description = form['description']
            measurements = [form['1'], form['2'], form['3']]
            service.update(set__name=name,
                            set__yob=yob,
                            set__gender =gender,
                            set__height= height,
                            set__phone=phone,
                            set__address = address,
                            set__status = status,
                            set__image = image,
                            set__description = description,
                            set__measurements=measurements)
            service.reload()
        return redirect(url_for('admin'))

@app.route('/sign-in', methods =['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        if 'loged-in' not in session:
            return render_template('sign-in.html')
        else:
            return render_template('error.html',error_code = "error_multi_login")
    elif request.method == 'POST':
        form = request.form
        email = form['email']
        match = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' ,email)
        if match == None:
            return render_template('error.html',error_code = "invalid_email")
        fullname = form['fullname']
        username = form['username']
        password = form['password']
        same_username = User.objects(username__exact= username)
        same_email = User.objects(email__exact= email)
        # print(type(same_email)) - queryset
        #check username and email exist
        if list(same_username) == [] and list(same_email) ==[]:
            new_user = User(fullname = fullname, email = email, username = username, password = password)
            new_user.save()
            session["loged-in"] = True
            session['user_id'] = str(new_user.id)
            return render_template('message.html', message='sign-in')
        elif list(same_email) != []:
            return render_template('error.html',error_code = "error_sign_in_email")
        else:
            return render_template('error.html',error_code = "error_sign_in_usermame")

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'loged-in' not in session:
            return render_template('login.html')
        else:
            return render_template('error.html',error_code = "error_multi_login")
    elif request.method =='POST':
        form = request.form
        username = form['username']
        password = form['password']
        # If can not get a match object, a exception raise => exception handling
        try:
            user = User.objects.get(username__exact = username, password__exact= password)
        except:
            user = None
        if user is not None:
            user = User.objects.get(username__exact = username, password__exact= password)
            session["loged-in"] = True
            session["user_id"] = str(user.id)
            return redirect(url_for('index'))
        else:
            return render_template('error.html',error_code = "error_login")

@app.route('/order/<order_service_id>')
def order(order_service_id):
    if (Service.objects.with_id(order_service_id)).status:
        new_order = Order(service_id =order_service_id, user_id =session["user_id"],time_ordered = datetime.now().strftime("%I:%M %p - %d/%m"), is_accepted =False )
        new_order.save()
        return render_template('message.html', message='ordered')
    else:
        return render_template('error.html',error_code = "error_order")

@app.route('/check-order')
def check_order():
    orders = Order.objects(is_accepted = False)
    return render_template("check-order.html", orders = orders)

@app.route('/request_accepted/<id_accepted>')
def request_accepted(id_accepted):
    order_accepted = Order.objects.with_id(id_accepted)
    order_accepted.update(set__is_accepted= True)
    order_accepted.reload()
    gmail = GMail('honganhc4e16@gmail.com','c4e162018')
    msg = Message("Thông báo chấp nhận yêu cầu",to=order_accepted.user_id.email,text="Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của 'Mùa Đông Không Lạnh'")
    gmail.send(msg)
    order_accepted.service_id.update(set__status=False)   #set status of service = False
    order_accepted.service_id.reload()
    return render_template('message.html', message='accepted')


@app.route('/logout')
def logout():
    if 'loged-in' in session:
        del session['loged-in']
        session["user_id"] = None
        return render_template('message.html', message='logout')
    else:
        return render_template('error.html',error_code = "error_logout")

if __name__ == '__main__':
  app.run(debug=True)
