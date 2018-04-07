from flask import Flask, render_template, request, redirect,url_for
from models.service import Service
import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender_i>')
def search_gender(gender_i):
    services = Service.objects(gender = gender_i)
    return render_template('services_gender.html', services_o = services)

@app.route('/detail/<id_to_find>')
def show_detail(id_to_find):
    service = Service.objects.with_id(id_to_find)
    print(id_to_find)
    return render_template('detail.html',service = service)

@app.route('/admin')
def admin():
    all_services = Service.objects()
    return render_template('admin.html', all_services = all_services)

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
        yob = form['yob']
        phone = form['phone number']
        gender = form['gender']

        new_service = Service(name = name, yob = yob, phone = phone, gender = gender)
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
            yob = form['yob']
            gender = form['gender']
            height = form['height']
            phone = form['phone']
            address = form['address']
            if form['status'] == 0:
                status = False
            else:
                status = True
            image = form['image']
            description = form['description']
            measurements = [form['1'], form['2'], form['3']]
            service.update(set__name=name, set__yob=yob, set__gender =gender, set__height= height, set__phone=phone,
                      set__address = address, set__status = status, set__image = image, set__description = description, set__measurements=measurements)
            service.reload()
        return redirect(url_for('admin'))



if __name__ == '__main__':
  app.run(debug=True)
