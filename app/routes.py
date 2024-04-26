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
    usuario = Usuario(nome=nome, email=email)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        usuario.nome = nome
        usuario.email = email
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", usuario=usuario)

@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('index'))






