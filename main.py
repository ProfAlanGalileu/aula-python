import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='src/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:aulaflask@localhost:3306/aula'
db = SQLAlchemy(app)

class usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True, index=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


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


@app.route("/users")
def users():
    users = usuario.query.all()
    return render_template('users.html', users=users)   

@app.route("/del_user/<int:id>")     
def del_user(id):
    user = usuario.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("users"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = usuario()
        user.nome = request.form["nome"]
        user.email = request.form["email"]
        user.password = request.form["senha"]
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users"))
    return render_template("register.html")
def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
