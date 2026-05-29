import sqlite3
import os

DATABASE_NAME = 'biblioteca.db'

def get_connection():
    """Retorna uma conexão com o banco de dados"""
    db_path = os.path.join(os.path.dirname(__file__), DATABASE_NAME)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Inicializa o banco de dados criando as tabelas necessárias"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabela de usuários (para login e gerenciamento)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_completo TEXT NOT NULL,
            codigo_matricula TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            tipo TEXT DEFAULT 'usuario',
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de livros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            isbn TEXT UNIQUE,
            ano_publicacao INTEGER,
            categoria TEXT,
            quantidade_total INTEGER DEFAULT 1,
            quantidade_disponivel INTEGER DEFAULT 1,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de empréstimos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            livro_id INTEGER NOT NULL,
            data_emprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_devolucao_prevista DATE,
            data_devolucao_real DATE,
            status TEXT DEFAULT 'ativo',
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
            FOREIGN KEY (livro_id) REFERENCES livros (id)
        )
    ''')
    
    # Tabela de dados importados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_importados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            conteudo TEXT,
            fonte TEXT,
            data_importacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Criar usuário administrador padrão
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome_completo, codigo_matricula, senha, tipo)
            VALUES ('Administrador', 'admin', 'admin', 'admin')
        ''')
    except sqlite3.IntegrityError:
        pass  # Usuário já existe
    
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

if __name__ == '__main__':
    init_database()
