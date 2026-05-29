import tkinter as tk
from tkinter import messagebox

class MenuUI:
    def __init__(self, root, usuario, callbacks):
        self.root = root
        self.usuario = usuario
        self.callbacks = callbacks
        self.root.title("Sistema de Biblioteca - Menu Principal")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.center_window()
        self.criar_widgets()
    
    def center_window(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def criar_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=30, pady=30)
        main_frame.pack(expand=True, fill='both')
        
        # Cabeçalho
        header_frame = tk.Frame(main_frame)
        header_frame.pack(fill='x', pady=(0, 30))
        
        tk.Label(header_frame, text="Sistema de Biblioteca", 
                font=('Arial', 20, 'bold')).pack()
        tk.Label(header_frame, text=f"Usuário: {self.usuario['nome_completo']}", 
                font=('Arial', 10)).pack(pady=(5, 0))
        
        # Frame de botões
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(expand=True)
        
        # Botões do menu
        button_config = {
            'font': ('Arial', 11),
            'width': 35,
            'height': 2,
            'bg': '#2196F3',
            'fg': 'white'
        }
        
        tk.Button(buttons_frame, text="Gerenciar Livros", 
                 command=self.callbacks['livros'], **button_config).pack(pady=5)
        
        tk.Button(buttons_frame, text="Gerenciar Usuários", 
                 command=self.callbacks['usuarios'], **button_config).pack(pady=5)
        
        tk.Button(buttons_frame, text="Gerenciar Empréstimos", 
                 command=self.callbacks['emprestimos'], **button_config).pack(pady=5)
        
        tk.Button(buttons_frame, text="Exportar Dados (JSON/ZIP)", 
                 command=self.callbacks['exportar'], **button_config).pack(pady=5)
        
        tk.Button(buttons_frame, text="Importar Dados da Web", 
                 command=self.callbacks['importar'], **button_config).pack(pady=5)
        
        tk.Button(buttons_frame, text="Sobre o Sistema", 
                 command=self.callbacks['sobre'], **button_config).pack(pady=5)
        
        # Botão Sair
        tk.Button(buttons_frame, text="Sair", 
                 command=self.sair, font=('Arial', 11), width=35, height=2,
                 bg='#f44336', fg='white').pack(pady=(15, 0))
    
    def sair(self):
        if messagebox.askyesno("Confirmar", "Deseja realmente sair?"):
            self.root.quit()
