from app import db
from werkzeug.security import generate_password_hash, check_password_hash

#classe para tabela de login
class User(db.Model):
    __tablename__ = 'login'

    id_login = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwordhash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.passwordhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)
    

#classe para tabela clientes
class Client(db.Model):
    
    __tablename__ = 'clientes'

    clientid = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120), unique = False, nullable = False)
    sobrenome = db.Column(db.String(120), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    

#classe para tabela de produto
class Product(db.Model):
    
    __tablename__ = 'produtos' 

    produto_id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(120), unique = True, nullable = False)
    descricao = db.Column(db.String(255), unique = False, nullable = False)
    categoria = db.Column(db.String(120), unique = False, nullable = False)
    valor = db.Column(db.Float, unique = False, nullable = False)
    estoque_disponivel = db.Column(db.Integer, unique = False, nullable = False)
    imagem = db.Column(db.LargeBinary, nullable=True)