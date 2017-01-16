from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import culqipy

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

    culqipy.API_KEY = "sk_test_UTCQSGcXW8bCyU59"

    charge = culqipy.Charge.create(
      address="Avenida Lima 1232",
      address_city="LIMA",
      amount=1000,
      country_code="PE",
      currency_code="PEN",
      email=email,
      first_name=first_name,
      installments=0,
      last_name=last_name,
      metadata="",
      phone_number=3333339,
      product_description="Venta de prueba",
      token_id=token)

    return jsonify(charge)

if __name__ == "__main__":
    app.run()
