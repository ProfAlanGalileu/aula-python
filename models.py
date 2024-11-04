from main import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

# Modelo Cafe
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)

# Modelo Venda
class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    id_cafe = db.Column(db.Integer, db.ForeignKey('cafe.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    data_venda = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    cliente = db.relationship('Cliente', backref=db.backref('vendas', lazy=True))
    cafe = db.relationship('Cafe', backref=db.backref('vendas', lazy=True))