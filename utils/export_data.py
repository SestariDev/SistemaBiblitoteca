import json
import zipfile
import os
from datetime import datetime
from tkinter import messagebox, filedialog
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_config import get_connection

def exportar_dados():
    """Exporta todos os dados do sistema em formato JSON e compacta em ZIP"""
    try:
        # Coletar dados de todas as tabelas
        conn = get_connection()
        cursor = conn.cursor()
        
        dados_completos = {}
        
        # Usuários
        cursor.execute('SELECT * FROM usuarios')
        usuarios = [dict(row) for row in cursor.fetchall()]
        dados_completos['usuarios'] = usuarios
        
        # Livros
        cursor.execute('SELECT * FROM livros')
        livros = [dict(row) for row in cursor.fetchall()]
        dados_completos['livros'] = livros
        
        # Empréstimos
        cursor.execute('SELECT * FROM emprestimos')
        emprestimos = [dict(row) for row in cursor.fetchall()]
        dados_completos['emprestimos'] = emprestimos
        
        # Dados importados
        cursor.execute('SELECT * FROM dados_importados')
        dados_importados = [dict(row) for row in cursor.fetchall()]
        dados_completos['dados_importados'] = dados_importados
        
        conn.close()
        
        # Adicionar metadados
        dados_completos['metadata'] = {
            'data_exportacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_usuarios': len(usuarios),
            'total_livros': len(livros),
            'total_emprestimos': len(emprestimos)
        }
        
        # Criar arquivo JSON temporário
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_filename = f'biblioteca_backup_{timestamp}.json'
        zip_filename = f'biblioteca_backup_{timestamp}.zip'
        
        # Perguntar onde salvar
        zip_path = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("Arquivo ZIP", "*.zip")],
            initialfile=zip_filename,
            title="Salvar Backup"
        )
        
        if not zip_path:
            return False, "Exportação cancelada."
        
        # Criar diretório temporário se necessário
        temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        json_path = os.path.join(temp_dir, json_filename)
        
        # Salvar JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(dados_completos, f, ensure_ascii=False, indent=2)
        
        # Criar arquivo ZIP
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(json_path, json_filename)
        
        # Remover arquivo JSON temporário
        os.remove(json_path)
        
        mensagem = f"""Dados exportados com sucesso!

Arquivo: {os.path.basename(zip_path)}
Local: {os.path.dirname(zip_path)}

Total de registros:
• Usuários: {len(usuarios)}
• Livros: {len(livros)}
• Empréstimos: {len(emprestimos)}
• Dados Importados: {len(dados_importados)}"""
        
        return True, mensagem
        
    except Exception as e:
        return False, f"Erro ao exportar dados: {str(e)}"


def mostrar_ui_exportacao(parent):
    """Mostra interface para exportação de dados"""
    if messagebox.askyesno("Exportar Dados", 
                          "Deseja exportar todos os dados do sistema em formato JSON/ZIP?"):
        sucesso, mensagem = exportar_dados()
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", mensagem)
