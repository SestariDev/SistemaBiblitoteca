import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_config import get_connection

class Usuario:
    @staticmethod
    def criar(nome_completo, codigo_matricula, senha, tipo='usuario'):
        """Cria um novo usuário"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO usuarios (nome_completo, codigo_matricula, senha, tipo)
                VALUES (?, ?, ?, ?)
            ''', (nome_completo, codigo_matricula, senha, tipo))
            conn.commit()
            return True, "Usuário criado com sucesso!"
        except Exception as e:
            return False, f"Erro ao criar usuário: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def listar():
        """Lista todos os usuários"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios ORDER BY nome_completo')
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios
    
    @staticmethod
    def buscar_por_id(usuario_id):
        """Busca um usuário por ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
        usuario = cursor.fetchone()
        conn.close()
        return usuario
    
    @staticmethod
    def atualizar(usuario_id, nome_completo, codigo_matricula, senha=None, tipo='usuario'):
        """Atualiza um usuário"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if senha:
                cursor.execute('''
                    UPDATE usuarios 
                    SET nome_completo = ?, codigo_matricula = ?, senha = ?, tipo = ?
                    WHERE id = ?
                ''', (nome_completo, codigo_matricula, senha, tipo, usuario_id))
            else:
                cursor.execute('''
                    UPDATE usuarios 
                    SET nome_completo = ?, codigo_matricula = ?, tipo = ?
                    WHERE id = ?
                ''', (nome_completo, codigo_matricula, tipo, usuario_id))
            conn.commit()
            return True, "Usuário atualizado com sucesso!"
        except Exception as e:
            return False, f"Erro ao atualizar usuário: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def deletar(usuario_id):
        """Deleta um usuário"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
            conn.commit()
            return True, "Usuário deletado com sucesso!"
        except Exception as e:
            return False, f"Erro ao deletar usuário: {str(e)}"
        finally:
            conn.close()
    
    @staticmethod
    def autenticar(codigo_matricula, senha):
        """Autentica um usuário"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM usuarios 
            WHERE codigo_matricula = ? AND senha = ?
        ''', (codigo_matricula, senha))
        usuario = cursor.fetchone()
        conn.close()
        return usuario
