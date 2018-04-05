from flask import Flask, render_template
from models.customer import Customer
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer/')
def show_all_customers():
    all_customers = Customer.objects()
    return render_template('all_customers.html',all_customers = all_customers)

@app.route('/customer/<int:gender>/')
def show_filtered_customers(gender):
    customers = Customer.objects(gender = gender, contacted = False)[:10]
    return render_template('f_customer.html',customers = customers, gender = gender)


if __name__ == '__main__':
  app.run(debug=True)
