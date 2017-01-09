from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from culqipy import culqi

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/charges', methods=['POST'])
def charge():
    token = request.form['token']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    culqiObject = culqi.Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")
    charge = culqiObject.createCharge("Avenida Lima 1232","LIMA",1000,"PE","PEN",email,first_name,0,last_name,"",3333339,"Venta de prueba",token)

    return jsonify(charge)

if __name__ == "__main__":
    app.run()
