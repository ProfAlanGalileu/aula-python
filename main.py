from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='src/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:aulaflask@localhost:3306/cafe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Cliente, Cafe, Venda

# Rota Inicial
@app.route('/')
def index():
    return render_template('base.html')

# Rota Clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_cliente = Cliente(nome=nome, email=email)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('clientes'))

    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

# Rota Cafés
@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        novo_cafe = Cafe(nome=nome, preco=preco)
        db.session.add(novo_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))

    cafes = Cafe.query.all()
    return render_template('cafes.html', cafes=cafes)

# Rota Vendas
@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        id_cafe = request.form['id_cafe']
        quantidade = request.form['quantidade']
        cafe = Cafe.query.get(id_cafe)
        total = cafe.preco * int(quantidade)
        nova_venda = Venda(id_cliente=id_cliente, id_cafe=id_cafe, quantidade=quantidade, total=total)
        db.session.add(nova_venda)
        db.session.commit()
        return redirect(url_for('vendas'))

    clientes = Cliente.query.all()
    cafes = Cafe.query.all()
    vendas = Venda.query.all()
    return render_template('vendas.html', vendas=vendas, clientes=clientes, cafes=cafes)

if __name__ == "__main__":
    main()
