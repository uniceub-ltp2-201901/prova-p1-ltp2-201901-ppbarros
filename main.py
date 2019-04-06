from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/listarProfessores/')
def professores():
    cursor = mysql.get_db().cursor()
    return render_template('professores.html', professores=get_professores(cursor))

@app.route('/exibirProfessor/<id>')
def mostrar_professor(id):
    cursor = mysql.get_db().cursor()
    return render_template('detalhe.html', detalhe=exibir_professor(cursor, id), disciplina=exibir_disciplina(cursor, id))

@app.route('/consultarPorTitulacao/<tit>')
def tit(tit):
    cursor = mysql.get_db().cursor()
    return render_template('titulacao.html', titulacao=tit, data=titulacao(cursor, tit))

@app.route('/calcularSalarioProfessor/<id>')
def consultar_salario(id):
    cursor = mysql.get_db().cursor()
    return render_template('salario.html', professor=nome(cursor, id), carga=salario(cursor, id))

@app.route('/consultarApenasComputacao')
def computacao():
    cursor = mysql.get_db().cursor()
    return render_template('computacao.html', prof=cic(cursor))


if __name__ == '__main__':
    app.run(debug=True)