from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
# sample secret key
app.secret_key = '\x03\x97\xff}\x06\x95\xbc\x1b\x978\xdb\x8b\xfd}\x0e\xeb\x10\xeb\xfe\x172J\x07d'


# add check login!
@app.route("/dashboard")
def dashboard():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

if __name__ == "__main__":

    # app.run(host='0.0.0.0', debug=True)
    app.run(debug=True)

