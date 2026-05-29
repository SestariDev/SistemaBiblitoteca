import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.usuario import Usuario

class UsuariosUI:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Gerenciamento de Usuários")
        self.window.geometry("900x600")
        self.window.transient(parent)
        
        self.center_window()
        self.criar_widgets()
        self.carregar_usuarios()
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def criar_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        tk.Label(main_frame, text="Gerenciamento de Usuários", 
                font=('Arial', 16, 'bold')).pack(pady=(0, 20))
        
        # Frame de botões de ação
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=(0, 10))
        
        tk.Button(btn_frame, text="Novo Usuário", command=self.novo_usuario,
                 bg='#4CAF50', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Editar", command=self.editar_usuario,
                 bg='#2196F3', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Deletar", command=self.deletar_usuario,
                 bg='#f44336', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Atualizar", command=self.carregar_usuarios,
                 bg='#FF9800', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        
        # Frame da tabela
        table_frame = tk.Frame(main_frame)
        table_frame.pack(expand=True, fill='both')
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(table_frame, orient='vertical')
        scrollbar_y.pack(side='right', fill='y')
        
        scrollbar_x = ttk.Scrollbar(table_frame, orient='horizontal')
        scrollbar_x.pack(side='bottom', fill='x')
        
        # Treeview
        self.tree = ttk.Treeview(table_frame, 
                                 columns=('ID', 'Nome', 'Matrícula', 'Tipo', 'Data'),
                                 show='headings',
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        # Configurar colunas
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nome', text='Nome Completo')
        self.tree.heading('Matrícula', text='Matrícula')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Data', text='Data Cadastro')
        
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Nome', width=250)
        self.tree.column('Matrícula', width=150, anchor='center')
        self.tree.column('Tipo', width=100, anchor='center')
        self.tree.column('Data', width=150, anchor='center')
        
        self.tree.pack(expand=True, fill='both')
        
        # Botão Fechar
        tk.Button(main_frame, text="Fechar", command=self.window.destroy,
                 font=('Arial', 10), padx=30, pady=8).pack(pady=(10, 0))
    
    def carregar_usuarios(self):
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Carregar usuários
        usuarios = Usuario.listar()
        for usuario in usuarios:
            self.tree.insert('', 'end', values=(
                usuario['id'],
                usuario['nome_completo'],
                usuario['codigo_matricula'],
                usuario['tipo'],
                usuario['data_cadastro'][:16] if usuario['data_cadastro'] else ''
            ))
    
    def novo_usuario(self):
        FormularioUsuarioUI(self.window, None, self.carregar_usuarios)
    
    def editar_usuario(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um usuário para editar!")
            return
        
        item = self.tree.item(selected[0])
        usuario_id = item['values'][0]
        FormularioUsuarioUI(self.window, usuario_id, self.carregar_usuarios)
    
    def deletar_usuario(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um usuário para deletar!")
            return
        
        item = self.tree.item(selected[0])
        usuario_id = item['values'][0]
        nome = item['values'][1]
        
        if messagebox.askyesno("Confirmar", f"Deseja realmente deletar o usuário '{nome}'?"):
            sucesso, mensagem = Usuario.deletar(usuario_id)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.carregar_usuarios()
            else:
                messagebox.showerror("Erro", mensagem)


class FormularioUsuarioUI:
    def __init__(self, parent, usuario_id, callback):
        self.window = tk.Toplevel(parent)
        self.usuario_id = usuario_id
        self.callback = callback
        self.window.title("Novo Usuário" if not usuario_id else "Editar Usuário")
        self.window.geometry("450x400")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.center_window()
        self.criar_widgets()
        
        if usuario_id:
            self.carregar_dados()
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def criar_widgets(self):
        main_frame = tk.Frame(self.window, padx=30, pady=30)
        main_frame.pack(expand=True, fill='both')
        
        # Nome Completo
        tk.Label(main_frame, text="Nome Completo:", font=('Arial', 10)).pack(anchor='w')
        self.entry_nome = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_nome.pack(fill='x', pady=(5, 15))
        
        # Código de Matrícula
        tk.Label(main_frame, text="Código de Matrícula:", font=('Arial', 10)).pack(anchor='w')
        self.entry_matricula = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_matricula.pack(fill='x', pady=(5, 15))
        
        # Senha
        tk.Label(main_frame, text="Senha:", font=('Arial', 10)).pack(anchor='w')
        self.entry_senha = tk.Entry(main_frame, show='*', font=('Arial', 10))
        self.entry_senha.pack(fill='x', pady=(5, 15))
        
        # Tipo
        tk.Label(main_frame, text="Tipo de Usuário:", font=('Arial', 10)).pack(anchor='w')
        self.combo_tipo = ttk.Combobox(main_frame, values=['usuario', 'admin'], 
                                       state='readonly', font=('Arial', 10))
        self.combo_tipo.set('usuario')
        self.combo_tipo.pack(fill='x', pady=(5, 25))
        
        # Botões
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack()
        
        tk.Button(btn_frame, text="Salvar", command=self.salvar,
                 bg='#4CAF50', fg='white', font=('Arial', 10), 
                 padx=20, pady=8).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.window.destroy,
                 bg='#f44336', fg='white', font=('Arial', 10), 
                 padx=20, pady=8).pack(side='left', padx=5)
    
    def carregar_dados(self):
        usuario = Usuario.buscar_por_id(self.usuario_id)
        if usuario:
            self.entry_nome.insert(0, usuario['nome_completo'])
            self.entry_matricula.insert(0, usuario['codigo_matricula'])
            self.combo_tipo.set(usuario['tipo'])
    
    def salvar(self):
        nome = self.entry_nome.get().strip()
        matricula = self.entry_matricula.get().strip()
        senha = self.entry_senha.get().strip()
        tipo = self.combo_tipo.get()
        
        if not nome or not matricula:
            messagebox.showwarning("Atenção", "Nome e matrícula são obrigatórios!")
            return
        
        if not self.usuario_id and not senha:
            messagebox.showwarning("Atenção", "Senha é obrigatória para novo usuário!")
            return
        
        if self.usuario_id:
            sucesso, mensagem = Usuario.atualizar(self.usuario_id, nome, matricula, 
                                                  senha if senha else None, tipo)
        else:
            sucesso, mensagem = Usuario.criar(nome, matricula, senha, tipo)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.callback()
            self.window.destroy()
        else:
            messagebox.showerror("Erro", mensagem)
