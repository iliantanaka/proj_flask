from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)


# Rota para pagina de Admin.
@app.route("/admin")
def admin():
    return "<p>Você está na página do Admin...</p>"


# Rota para hospede.
@app.route("/guest/<guest>")
def guest(guest):
    return 'Ola, %s' % guest


# Redirecionar para admin ou hospede.
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
