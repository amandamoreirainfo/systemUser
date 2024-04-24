from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Usuario

with app.app_context():
    print(db.create_all())

@app.route('/')
def index():
    #usuarios = Usuario.query.all()
    return render_template('index.html')

@app.route("/register")
def createUser():
    return render_template('login.html')

@app.route('/added', methods=['POST'])
def addedUser():
    nome = request.form['nome']
    email = request.form['email']
    usuario = Usuario(nome=nome, email=email)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('index'))


#criar tablea no banco de dados

#@app.cli.command()
#def createTables():
  #  db.create_all()
 #   print("Tabela criada com sucesso. ")

#if __name__ == '__main__':
   # app.run()


