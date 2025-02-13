import joblib
import numpy as np
from csv import reader
from flask import *
app = Flask(__name__)
ob = joblib.load('insurance_model.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/prediction')
def prediction():
    return render_template('predict.html')

@app.route('/prediction', methods=['POST'])
def madhu():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    num3 = int(request.form['num3'])
    num4 = int(request.form['num4'])
    num5 = int(request.form['num5'])
    num6 = int(request.form['num6'])
    num7 = int(request.form['num7'])
    num8 = int(request.form['num8'])

    a = [[num1,num2,num3,num4,num5,num6,num7,num8]]
    predd = ob.predict(a)


    return redirect(url_for('result',result1=predd))

@app.route('/result')
def result():
    predd = request.args.get('result1')
    return render_template('result.html',result1=predd)

if __name__ == '__main__':
    app.run(debug=True)
