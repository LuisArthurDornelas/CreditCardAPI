from flask import Flask, render_template, request, redirect, url_for
import api
from datetime import datetime
from api import validate_credit_card

app = Flask(__name__)

@app.route('/validate', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        card_number = request.form['card-number']
        expiry = request.form['expiry']
        cvv = request.form['cvv']

        is_valid = validate_credit_card(card_number, expiry, cvv)

        if is_valid:
            api.validate_credit_card(card_number, expiry, cvv)
            return render_template('success.html', message='Credit card is valid')
        else:
            return render_template('failure.html', message='Invalid credit card data')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
