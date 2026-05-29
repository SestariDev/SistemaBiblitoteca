"""
Sistema de Gerenciamento de Biblioteca
Projeto da disciplina Tópicos Especiais em Informática
Fatec Ribeirão Preto - ADS
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Adicionar diretórios ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_config import init_database
from ui.login import LoginUI
from ui.menu import MenuUI
from ui.sobre import SobreUI
from utils.usuarios_ui import UsuariosUI
from ui.livros_ui import LivrosUI
from ui.emprestimos_ui import EmprestimosUI
from utils.export_data import mostrar_ui_exportacao
from utils.import_data import ImportarDadosUI


class SistemaBiblioteca:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Esconder janela principal
        self.usuario_logado = None
        
        # Inicializar banco de dados
        init_database()
        
        # Mostrar tela de login
        self.mostrar_login()
    
    def mostrar_login(self):
        """Exibe a tela de login"""
        login_window = tk.Toplevel(self.root)
        LoginUI(login_window, self.on_login_success)
    
    def on_login_success(self, usuario):
        """Callback chamado após login bem-sucedido"""
        self.usuario_logado = usuario
        
        # Fechar todas as janelas abertas exceto a principal
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()
        
        # Mostrar menu principal
        self.mostrar_menu()
    
    def mostrar_menu(self):
        """Exibe o menu principal"""
        menu_window = tk.Toplevel(self.root)
        
        callbacks = {
            'usuarios': lambda: UsuariosUI(menu_window),
            'livros': lambda: LivrosUI(menu_window),
            'emprestimos': lambda: EmprestimosUI(menu_window),
            'exportar': lambda: mostrar_ui_exportacao(menu_window),
            'importar': lambda: ImportarDadosUI(menu_window),
            'sobre': lambda: SobreUI(menu_window)
        }
        
        MenuUI(menu_window, self.usuario_logado, callbacks)
    
    def run(self):
        """Inicia a aplicação"""
        self.root.mainloop()


def main():
    """Função principal"""
    try:
        app = SistemaBiblioteca()
        app.run()
    except Exception as e:
        messagebox.showerror("Erro Fatal", f"Erro ao iniciar aplicação:\n{str(e)}")
        raise


if __name__ == '__main__':
    main()
