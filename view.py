import sqlite3 as lite

con = lite.connect('dados.db')


# --------------------------   Inserts  --------------------------
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO categoria (nome) VALUES(?)"
        cur.execute(query,i)

def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO receitas (idCategoria,adicionado_em,valor) VALUES(?,?,?)"
        cur.execute(query, i)

def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO gastos (idCategoria,retirado_em,valor) VALUES(?,?,?)"
        cur.execute(query, i)


# --------------------------   Deletes  --------------------------

def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query,i)

def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM gastos WHERE id=?"
        cur.execute(query,i)

# --------------------------   Selects  --------------------------


def selecionar_categorias():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM categoria")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)
    return lista_itens

def selecionar_receitas(i):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM receita")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)
    return lista_itens

def selecionar_gastos(i):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM gastos")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)
    return lista_itens

print(selecionar_categorias())