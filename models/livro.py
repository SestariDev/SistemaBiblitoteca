import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_config import get_connection

class Livro:
    @staticmethod
    def criar(titulo, autor, isbn, ano_publicacao, categoria, quantidade_total):
        """Cria um novo livro"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO livros (titulo, autor, isbn, ano_publicacao, categoria, 
                                   quantidade_total, quantidade_disponivel)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (titulo, autor, isbn, ano_publicacao, categoria, quantidade_total, quantidade_total))
            conn.commit()
            return True, "Livro cadastrado com sucesso!"
        except Exception as e:
            return False, f"Erro ao cadastrar livro: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def listar():
        """Lista todos os livros"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM livros ORDER BY titulo')
        livros = cursor.fetchall()
        conn.close()
        return livros
    
    @staticmethod
    def buscar_por_id(livro_id):
        """Busca um livro por ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM livros WHERE id = ?', (livro_id,))
        livro = cursor.fetchone()
        conn.close()
        return livro
    
    @staticmethod
    def atualizar(livro_id, titulo, autor, isbn, ano_publicacao, categoria, quantidade_total):
        """Atualiza um livro"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Calcula a nova quantidade disponível
            cursor.execute('SELECT quantidade_total, quantidade_disponivel FROM livros WHERE id = ?', (livro_id,))
            livro_atual = cursor.fetchone()
            diferenca = quantidade_total - livro_atual['quantidade_total']
            nova_disponivel = livro_atual['quantidade_disponivel'] + diferenca
            
            cursor.execute('''
                UPDATE livros 
                SET titulo = ?, autor = ?, isbn = ?, ano_publicacao = ?, 
                    categoria = ?, quantidade_total = ?, quantidade_disponivel = ?
                WHERE id = ?
            ''', (titulo, autor, isbn, ano_publicacao, categoria, quantidade_total, nova_disponivel, livro_id))
            conn.commit()
            return True, "Livro atualizado com sucesso!"
        except Exception as e:
            return False, f"Erro ao atualizar livro: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def deletar(livro_id):
        """Deleta um livro"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
            conn.commit()
            return True, "Livro deletado com sucesso!"
        except Exception as e:
            return False, f"Erro ao deletar livro: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def atualizar_disponibilidade(livro_id, quantidade_emprestada):
        """Atualiza a quantidade disponível após empréstimo"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE livros 
                SET quantidade_disponivel = quantidade_disponivel - ?
                WHERE id = ?
            ''', (quantidade_emprestada, livro_id))
            conn.commit()
            return True
        except Exception as e:
            return False
        finally:
            conn.close()
    
    @staticmethod
    def devolver_livro(livro_id):
        """Devolve um livro aumentando a quantidade disponível"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE livros 
                SET quantidade_disponivel = quantidade_disponivel + 1
                WHERE id = ?
            ''', (livro_id,))
            conn.commit()
            return True
        except Exception as e:
            return False
        finally:
            conn.close()
