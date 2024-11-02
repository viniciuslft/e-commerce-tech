from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from postgres import connect


app = Flask(__name__)



#registro do usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(str(password)) #gera o hash da senha
        #dataNascimento = request.form['dataN']

        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("insert into login (email, passwordhash) values (%s, %s)" , (email, hashed_password))
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

        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("select passwordhash from login where email = %s", (email,))
            user = cur.fetchone()

            cur.close()
            conn.close()

            if user:
                hashedPassword = user[0]

                if check_password_hash(hashedPassword, password):
                    flash('Login realizado com sucesso')
                    print("Login realizado com sucesso")
                    return redirect(url_for('index'))
                else:
                    flash('Senha incorreta')
                    return render_template('login.html')
            else:
                flash('email não encontrado')
                return render_template('login.html')

        except Exception as e:
            flash('Erro ao fazer o login' + str(e))
            return render_template('login.html')
        
    return render_template('login.html')


@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
        

    