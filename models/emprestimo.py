import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_config import get_connection
from datetime import datetime, timedelta

class Emprestimo:
    @staticmethod
    def criar(usuario_id, livro_id, dias_emprestimo=14):
        """Cria um novo empréstimo"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Verifica disponibilidade
            cursor.execute('SELECT quantidade_disponivel FROM livros WHERE id = ?', (livro_id,))
            livro = cursor.fetchone()
            if not livro or livro['quantidade_disponivel'] <= 0:
                return False, "Livro não disponível para empréstimo!"
            
            # Cria o empréstimo
            data_devolucao = (datetime.now() + timedelta(days=dias_emprestimo)).date()
            cursor.execute('''
                INSERT INTO emprestimos (usuario_id, livro_id, data_devolucao_prevista, status)
                VALUES (?, ?, ?, 'ativo')
            ''', (usuario_id, livro_id, data_devolucao))
            
            # Atualiza disponibilidade do livro
            cursor.execute('''
                UPDATE livros 
                SET quantidade_disponivel = quantidade_disponivel - 1
                WHERE id = ?
            ''', (livro_id,))
            
            conn.commit()
            return True, f"Empréstimo realizado! Devolução prevista: {data_devolucao}"
        except Exception as e:
            conn.rollback()
            return False, f"Erro ao realizar empréstimo: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def listar():
        """Lista todos os empréstimos com informações de usuário e livro"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT e.*, u.nome_completo, u.codigo_matricula, l.titulo, l.autor
            FROM emprestimos e
            JOIN usuarios u ON e.usuario_id = u.id
            JOIN livros l ON e.livro_id = l.id
            ORDER BY e.data_emprestimo DESC
        ''')
        emprestimos = cursor.fetchall()
        conn.close()
        return emprestimos
    
    @staticmethod
    def buscar_por_id(emprestimo_id):
        """Busca um empréstimo por ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT e.*, u.nome_completo, l.titulo
            FROM emprestimos e
            JOIN usuarios u ON e.usuario_id = u.id
            JOIN livros l ON e.livro_id = l.id
            WHERE e.id = ?
        ''', (emprestimo_id,))
        emprestimo = cursor.fetchone()
        conn.close()
        return emprestimo
    
    @staticmethod
    def devolver(emprestimo_id):
        """Registra a devolução de um livro"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Busca o empréstimo
            cursor.execute('SELECT livro_id, status FROM emprestimos WHERE id = ?', (emprestimo_id,))
            emprestimo = cursor.fetchone()
            
            if not emprestimo:
                return False, "Empréstimo não encontrado!"
            
            if emprestimo['status'] == 'devolvido':
                return False, "Este livro já foi devolvido!"
            
            # Atualiza o empréstimo
            cursor.execute('''
                UPDATE emprestimos 
                SET data_devolucao_real = CURRENT_TIMESTAMP, status = 'devolvido'
                WHERE id = ?
            ''', (emprestimo_id,))
            
            # Atualiza disponibilidade do livro
            cursor.execute('''
                UPDATE livros 
                SET quantidade_disponivel = quantidade_disponivel + 1
                WHERE id = ?
            ''', (emprestimo['livro_id'],))
            
            conn.commit()
            return True, "Devolução registrada com sucesso!"
        except Exception as e:
            conn.rollback()
            return False, f"Erro ao registrar devolução: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def deletar(emprestimo_id):
        """Deleta um empréstimo (apenas se não estiver ativo)"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT status FROM emprestimos WHERE id = ?', (emprestimo_id,))
            emprestimo = cursor.fetchone()
            
            if emprestimo and emprestimo['status'] == 'ativo':
                return False, "Não é possível deletar um empréstimo ativo! Registre a devolução primeiro."
            
            cursor.execute('DELETE FROM emprestimos WHERE id = ?', (emprestimo_id,))
            conn.commit()
            return True, "Empréstimo deletado com sucesso!"
        except Exception as e:
            return False, f"Erro ao deletar empréstimo: {str(e)}"
        finally:
            conn.close()
