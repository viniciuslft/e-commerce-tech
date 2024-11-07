from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from postgres import connect


app = Flask(__name__)
app.secret_key = '4b7f6d2e1c9a8b7f6d2e1c9a8b7'


#registro do usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
       
        hashed_password = generate_password_hash(password) #gera o hash da senha
        #dataNascimento = request.form['dataN']

        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO login (email, passwordhash) VALUES (%s, %s)", (email, hashed_password))
            #cur.execute("insert into clientes (nome, sobrenome, email) values (teste, teste, '%s')", (email))
            conn.commit()
            cur.close()
            conn.close()

            flash('Cadastro realizado com sucesso!')
            print('Cadastro realizado')
            return render_template('login.html')
        
        except Exception as e:
            flash('Erro ao cadastrar: ' + str(e))
            return render_template('signup.html')
    return render_template('signup.html')
    



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Email inserido: {email}")
        print(f"Senha inserida: {password}")

        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("SELECT passwordhash FROM login WHERE email = %s", (email,))
            user = cur.fetchone()
            cur.close()
            conn.close()

            if user:
                hashed_password = user[0]
                
                # Verifica se a senha inserida confere com o hash armazenado
                if check_password_hash(hashed_password, password):
                    session['user'] = email
                    flash('Login realizado com sucesso!')
                    return redirect(url_for('index'))  # Redireciona para a página inicial (index)
                else:
                    flash('Senha incorreta')
                    print('Senha incorreta durante a verificação')  # Adicionando um print aqui
                    return render_template('login.html')
            else:
                flash('Email não encontrado')
                print('Email não encontrado no banco de dados')  # Adicionando um print aqui
                return render_template('login.html')

        except Exception as e:
            flash('Erro ao fazer o login: ' + str(e))
            print('Erro ao fazer login ' + str(e))
            return render_template('login.html')

    return render_template('login.html')


@app.route('/index')
def index():

    user_email = session.get('user')  # Obtém o e-mail do usuário da sessão, se disponível
    welcome_message = f"Bem-vindo, {user_email}" if user_email else None
    return render_template('index.html', welcome_message=welcome_message)


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logout feito com sucesso')
    return redirect(url_for('logout'))



if __name__ == '__main__':
    app.run(debug=True)
        

    