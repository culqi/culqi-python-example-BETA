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
    if request.method == 'POST':
        token = request.form['token']
        installments = request.form['installments']

        culqipy.API_KEY = "sk_test_UTCQSGcXW8bCyU59"

        dir_charge = {'amount': 3500,
                      'capture': True,
                      'currency_code': 'PEN',
                      'description': 'Culqi Store',
                      'email': 'wmuro@me.com',
                      'installments': installments,
                      'metadata': {'order_id': '1234'},
                      'source_id': token}

        charge = culqipy.Charge.create(dir_charge)

        return jsonify(charge)

    return jsonify({'error': 'nopost'})

if __name__ == "__main__":
    app.run()
