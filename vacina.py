import sqlite3
from datetime import datetime

def criar_banco_e_tabela():
    conn = sqlite3.connect('teste1.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_cadastrada TEXT
        )
    ''')
    
    data_exemplo = datetime.now().strftime('2024-09-14')
    
    cursor.execute('''
        INSERT OR REPLACE INTO pessoas (id, data_cadastrada)
        VALUES (1, ?)
    ''', (data_exemplo,))
    
    conn.commit()
    conn.close()


criar_banco_e_tabela()

print("Banco de dados 'teste1.db' criado e tabela 'pessoas' inicializada com sucesso!")

