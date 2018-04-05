import mlab
from models.service import Service
from flask import *

app = Flask(__name__)
mlab.connect()


# Create a document

# new_service = Service(name = 'Kiều Anh', yob = 1993, gender = 0, height = 160, phone = '0987654321', address = 'Hà Nội', status = True)
# new_service = Service(name = 'Hera', yob = 1994, gender = 0, height = 150, phone = '0987654421', address = 'Hà Nội', status = True)
#new_service = Service(name = 'Linh Ka', yob = 2002, gender = 0, height = 148, phone = '0987654322', address = 'Hà Đông', status = False)
# new_service = Service(name = 'Tuấn Anh', yob = 2000, gender =1, height = 171, phone = '0987654122', address = 'Hà Đông', status = True)
# new_service = Service(name = 'Hòa Threesome', yob = 1999, gender =1, height = 175, phone = '0987754122', address = 'Sài Gòn', status = True)
# new_service = Service(name = 'Nhi Chan Chan', yob = 2002, gender = 0, height = 160, phone = '0987654332', address = 'Huế', status = False)
# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(yob__lte=1998, gender=gender,address__icontains='hà Nội')
    return render_template('search.html', all_services = all_services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html',services = services)

@app.route('/delete/<service_id>')
def delete_f(service_id):
    service_to_del = Service.objects.with_id(service_id)
    if service_to_del is None:
        return "Not found"
    else:
        service_to_del.delete()
    return redirect(url_for('admin'))

@app.route('/new_service', methods= ['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template("new-service.html")
    elif request.method=="POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']

        new_service = Service(name = name, yob = yob, address = address)
        new_service.save()
        return redirect(url_for('admin'))


if __name__ == '__main__':
  app.run(debug=True)
