from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Usuario

@app.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@app.route("/register")
def createUser():
    return render_template('register.html')

@app.route('/added', methods=['POST'])
def addedUser():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome=nome, email=email, senha=senha)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", usuario=usuario)

@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email and senha:
            usuario = Usuario.query.filter_by(email=email, senha=senha).first()
            if usuario:
                return redirect(url_for('index'))
            else:
                return "Email ou senha incorretos."
    return render_template("login.html")
















