# Importando SQlite
import sqlite3 as lite

# Criando conexao
con = lite.connect('dados.db')

# criando tabela de categorias

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS receita (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idCategoria INTEGER,
    adicionado_en DATE,
    valor DECIMAL,
    FOREIGN KEY (idCategoria) REFERENCES categoria (id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS gastos (    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idCategoria INTEGER,
        retirado_em DATE,
        valor DECIMAL, 
        FOREIGN KEY (idCategoria) REFERENCES categoria (id)
    )
""")