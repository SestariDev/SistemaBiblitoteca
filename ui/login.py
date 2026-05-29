import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.usuario import Usuario

class LoginUI:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.root.title("Sistema de Biblioteca - Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Centralizar janela
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
        main_frame = tk.Frame(self.root, padx=40, pady=40)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        title_label = tk.Label(main_frame, text="Sistema de Biblioteca", 
                               font=('Arial', 18, 'bold'))
        title_label.pack(pady=(0, 30))
        
        # Código de Matrícula
        tk.Label(main_frame, text="Código de Matrícula:", font=('Arial', 10)).pack(anchor='w')
        self.entry_matricula = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_matricula.pack(fill='x', pady=(5, 15))
        self.entry_matricula.focus()
        
        # Senha
        tk.Label(main_frame, text="Senha:", font=('Arial', 10)).pack(anchor='w')
        self.entry_senha = tk.Entry(main_frame, show='*', font=('Arial', 10))
        self.entry_senha.pack(fill='x', pady=(5, 25))
        
        # Botão de Login
        btn_login = tk.Button(main_frame, text="Entrar", command=self.fazer_login,
                              font=('Arial', 11, 'bold'), bg='#4CAF50', fg='white',
                              padx=20, pady=10)
        btn_login.pack()
        
        # Bind Enter key
        self.entry_senha.bind('<Return>', lambda e: self.fazer_login())
        self.entry_matricula.bind('<Return>', lambda e: self.entry_senha.focus())
        
        # Info
        info_label = tk.Label(main_frame, text="Usuário padrão: admin / admin", 
                             font=('Arial', 8), fg='gray')
        info_label.pack(side='bottom', pady=(20, 0))
    
    def fazer_login(self):
        matricula = self.entry_matricula.get().strip()
        senha = self.entry_senha.get().strip()
        
        if not matricula or not senha:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
            return
        
        usuario = Usuario.autenticar(matricula, senha)
        
        if usuario:
            messagebox.showinfo("Sucesso", f"Bem-vindo(a), {usuario['nome_completo']}!")
            self.on_login_success(usuario)
        else:
            messagebox.showerror("Erro", "Matrícula ou senha incorretos!")
            self.entry_senha.delete(0, tk.END)
            self.entry_matricula.focus()
