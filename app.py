from flask import Flask, render_template, request, redirect, url_for
import api

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['name']
        idade = request.form['age']
        api.save_data(nome, idade)
        return redirect(url_for('thanks'))
    return render_template('form.html')

@app.route('/thanks')
def thanks():
    return 'Succesfully sent data!'

if __name__ == '__main__':
    app.run(debug=True)
