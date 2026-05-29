import tkinter as tk
from tkinter import ttk

class SobreUI:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Sobre o Sistema")
        self.window.geometry("600x500")
        self.window.resizable(False, False)
        self.window.transient(parent)
        self.window.grab_set()
        
        self.center_window()
        self.criar_widgets()
    
    def center_window(self):
        """Centraliza a janela na tela"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def criar_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.window, padx=30, pady=30)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        tk.Label(main_frame, text="Sistema de Gerenciamento de Biblioteca", 
                font=('Arial', 16, 'bold')).pack(pady=(0, 20))
        
        # Frame de informações
        info_frame = tk.Frame(main_frame, relief='groove', borderwidth=2, padx=20, pady=20)
        info_frame.pack(fill='both', expand=True)
        
        # Informações do Projeto
        tk.Label(info_frame, text="INFORMAÇÕES DO PROJETO", 
                font=('Arial', 12, 'bold'), fg='#2196F3').pack(pady=(0, 10))
        
        projeto_info = """
        Tema: Sistema de Gerenciamento de Biblioteca
        
        Objetivo: Desenvolver uma aplicação em Python para gerenciar
        o acervo de uma biblioteca, incluindo cadastro de livros,
        usuários e controle de empréstimos.
        
        Funcionalidades:
        • Cadastro e gerenciamento de livros
        • Cadastro e gerenciamento de usuários
        • Controle de empréstimos e devoluções
        • Exportação de dados em formato JSON/ZIP
        • Importação de dados da web
        
        Disciplina: Tópicos Especiais em Informática
        Instituição: Fatec Ribeirão Preto
        """
        
        tk.Label(info_frame, text=projeto_info, font=('Arial', 9), 
                justify='left').pack(anchor='w', pady=(0, 20))
        
        # Separador
        ttk.Separator(info_frame, orient='horizontal').pack(fill='x', pady=10)
        
        # Informações dos Desenvolvedores
        tk.Label(info_frame, text="DESENVOLVEDORES", 
                font=('Arial', 12, 'bold'), fg='#2196F3').pack(pady=(10, 10))
        
        # NOTA: Altere aqui com suas informações
        dev_info = """
        Nome: [SEU NOME COMPLETO]
        Matrícula: [SEU CÓDIGO DE MATRÍCULA]
        
        Nome: [NOME DO PARCEIRO (se em dupla)]
        Matrícula: [MATRÍCULA DO PARCEIRO (se em dupla)]
        """
        
        tk.Label(info_frame, text=dev_info, font=('Arial', 9), 
                justify='center').pack(pady=(0, 10))
        
        # Versão
        tk.Label(main_frame, text="Versão 1.0 - Maio/2026", 
                font=('Arial', 8), fg='gray').pack(side='bottom', pady=(10, 0))
        
        # Botão Voltar
        tk.Button(main_frame, text="Voltar", command=self.window.destroy,
                 font=('Arial', 10), bg='#2196F3', fg='white',
                 padx=30, pady=8).pack(side='bottom')
