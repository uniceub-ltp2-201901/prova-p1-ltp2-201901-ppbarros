def get_professores(cursor):
    cursor.execute(f'select nome, idprofessor from professor order by nome asc')
    professores = cursor.fetchall()
    cursor.close()
    return professores


def exibir_professor(cursor, id):
    cursor.execute(f'select nome, datanasc, nomemae, titulacao, idprofessor from professor where idprofessor = {id}')
    professor = cursor.fetchone()
    return professor

def exibir_disciplina(cursor, id):
    cursor.execute(f'select nome, curso, cargahoraria from disciplina where idprofessor = {id}')
    disciplinas = cursor.fetchall()
    cursor.close()
    return disciplinas

def titulacao(cursor, tit):
    cursor.execute(f'select nome, idprofessor from professor where titulacao = {tit} order by nome asc')
    professores = cursor.fetchall()
    cursor.close()
    return professores

def cic(cursor):
    cursor.execute('select distinct professor.nome from professor, disciplina where disciplina.curso = "Ciência da Computação" and professor.idprofessor = disciplina.idprofessor')
    professor = cursor.fetchall()
    return professor

def salario(cursor, id):
    cursor.execute(f'select sum(cargahoraria) from disciplina where idprofessor = {id}')
    carga = cursor.fetchone()
    cursor.close()
    return carga

def nome(cursor, id):
    cursor.execute(f'select nome from professor where idprofessor = {id}')
    professor = cursor.fetchone()
    return professor
