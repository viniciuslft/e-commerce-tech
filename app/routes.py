from flask import Blueprint, render_template, request, flash, redirect, url_for,session
from app import db
from app.models import User, Client, Product

auth_bp = Blueprint('auth', __name__)


# Cadastro de usuário
@auth_bp.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('As senhas não coincidem.', 'danger')
            return render_template('signup.html')

        if User.query.filter_by(email=email).first():
            flash('Email já registrado.', 'danger')
            return render_template('signup.html')

        try:
            new_user = User(email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            

            new_client = Client(email = email, nome = email)
            db.session.add(new_client)
            db.session.commit()

            flash("Cadastro realizado com sucesso!", 'success')
            return redirect(url_for('auth.login'))
        
        except Exception as e:
            print("Houve um erro de conexação com o banco de dados: " + str(e))

    return render_template('signup.html')


#cadastro de produto
@auth_bp.route('/productRegister', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')

        if Product.query.filter_by(nome = name).first():
            flash('Produto ja cadastrado')
            return render_template()
        
        try:
            new_product = Product(nome = name, descricao = description, valor = price)
            db.session.add(new_product)
            db.session.commit()

        except Exception as e:
            print('Houve um erro de conexção com o banco de dados' + e)


# Login de usuário
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user'] = user.email
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Email ou senha incorretos.', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)  # Remove o e-mail da sessão
    flash('Você saiu com sucesso!', 'success')
    return redirect(url_for('main.index'))  # Redireciona para a página inicial




# Página principal
main_bp = Blueprint('main', __name__)

@main_bp.route('/index')
def index():
    user_email = session.get('user')
    print(user_email)
    return render_template('index.html', user_email=user_email)

