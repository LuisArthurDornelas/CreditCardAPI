from flask import Flask, render_template, request, redirect, url_for
import api

app = Flask(__name__)

@app.route('/validate', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        card_number = request.form['card-number']
        expiry = request.form['expiry']
        cvv = request.form['cvv']
        api.save_data(name, card_number, expiry, cvv)
        return redirect(url_for('thanks'))
    return render_template('form.html')

@app.route('/thanks')
def thanks():
    return 'Succesfully sent data!'

if __name__ == '__main__':
    app.run(debug=True)
