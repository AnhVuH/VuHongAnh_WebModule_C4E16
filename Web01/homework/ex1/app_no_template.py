from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<int:weight>kg/<int:height>cm')
def calc_BMI(weight,height):
    bmi = weight/((height*0.01)**2)
    return 'Your BMI = {:.2f}. '.format(bmi)  + 'You are '+ ('Severely underweight' if bmi < 16 \
    else 'Underweight' if 16 <= bmi < 18.5 \
    else 'Normal' if 18.5 <= bmi < 25 \
    else 'Overweight' if 25 <= bmi < 30 \
    else 'Obese')

if __name__ == '__main__':
  app.run( debug=True)
