from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bmi/<int:weight>kg/<int:height>cm')
def calc_BMI(weight, height):
    bmi = weight/((height*0.01)**2)
    condition = 'Severely underweight' if bmi < 16 \
    else 'Underweight' if 16 <= bmi < 18.5 \
    else 'Normal' if 18.5 <= bmi < 25 \
    else 'Overweight' if 25 <= bmi < 30 \
    else 'Obese'
    return render_template('bmi.html', bmi = '{:.1f}'.format(bmi), condition = condition)

if __name__ == '__main__':
    app.run(debug =1)
