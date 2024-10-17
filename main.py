import os
from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder='src/templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre/<nome>")
def sobre(nome):
    return render_template('sobre.html', nome=nome)

@app.route("/login",  methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        return render_template('index.html', email=email,senha=senha)
    else:
        return render_template("login.html")

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
