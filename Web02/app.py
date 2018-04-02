import mlab
from models.service import Service
from flask import Flask, render_template

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

if __name__ == '__main__':
  app.run(debug=True)
