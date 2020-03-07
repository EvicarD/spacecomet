from flask import Flask, request, session
from flask import render_template
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def index():
    LIGHT_YEAR_SEC = 299792.458
    result = 0
    if request.method == 'POST':
        username = request.form['username']
        result = int(username) * LIGHT_YEAR_SEC
    return render_template('index.html', name='home', result=result)


@app.route('/facts')
def facts():
    return render_template('facts.html', name='facts')


@app.route('/ogle')
def ogle():
    return render_template('ogletr.html', name='ogle')
