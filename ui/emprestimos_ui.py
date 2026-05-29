import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.emprestimo import Emprestimo
from models.usuario import Usuario
from models.livro import Livro

class EmprestimosUI:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Gerenciamento de Empréstimos")
        self.window.geometry("1100x600")
        self.window.transient(parent)
        
        self.center_window()
        self.criar_widgets()
        self.carregar_emprestimos()
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def criar_widgets(self):
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        tk.Label(main_frame, text="Gerenciamento de Empréstimos", 
                font=('Arial', 16, 'bold')).pack(pady=(0, 20))
        
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=(0, 10))
        
        tk.Button(btn_frame, text="Novo Empréstimo", command=self.novo_emprestimo,
                 bg='#4CAF50', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Registrar Devolução", command=self.devolver_livro,
                 bg='#2196F3', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Deletar", command=self.deletar_emprestimo,
                 bg='#f44336', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Atualizar", command=self.carregar_emprestimos,
                 bg='#FF9800', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        
        table_frame = tk.Frame(main_frame)
        table_frame.pack(expand=True, fill='both')
        
        scrollbar_y = ttk.Scrollbar(table_frame, orient='vertical')
        scrollbar_y.pack(side='right', fill='y')
        
        scrollbar_x = ttk.Scrollbar(table_frame, orient='horizontal')
        scrollbar_x.pack(side='bottom', fill='x')
        
        self.tree = ttk.Treeview(table_frame, 
                                 columns=('ID', 'Usuário', 'Matrícula', 'Livro', 
                                         'Data Emp.', 'Prev. Devol.', 'Data Devol.', 'Status'),
                                 show='headings',
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        self.tree.heading('ID', text='ID')
        self.tree.heading('Usuário', text='Usuário')
        self.tree.heading('Matrícula', text='Matrícula')
        self.tree.heading('Livro', text='Livro')
        self.tree.heading('Data Emp.', text='Data Empréstimo')
        self.tree.heading('Prev. Devol.', text='Previsão Devolução')
        self.tree.heading('Data Devol.', text='Data Devolução')
        self.tree.heading('Status', text='Status')
        
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Usuário', width=150)
        self.tree.column('Matrícula', width=100, anchor='center')
        self.tree.column('Livro', width=200)
        self.tree.column('Data Emp.', width=130, anchor='center')
        self.tree.column('Prev. Devol.', width=130, anchor='center')
        self.tree.column('Data Devol.', width=130, anchor='center')
        self.tree.column('Status', width=100, anchor='center')
        
        self.tree.pack(expand=True, fill='both')
        
        tk.Button(main_frame, text="Fechar", command=self.window.destroy,
                 font=('Arial', 10), padx=30, pady=8).pack(pady=(10, 0))
    
    def carregar_emprestimos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        emprestimos = Emprestimo.listar()
        for emp in emprestimos:
            # Destacar empréstimos atrasados
            tags = ()
            if emp['status'] == 'ativo':
                from datetime import datetime
                data_prev = datetime.strptime(emp['data_devolucao_prevista'], '%Y-%m-%d').date()
                if data_prev < datetime.now().date():
                    tags = ('atrasado',)
            
            self.tree.insert('', 'end', values=(
                emp['id'],
                emp['nome_completo'],
                emp['codigo_matricula'],
                emp['titulo'],
                emp['data_emprestimo'][:16] if emp['data_emprestimo'] else '',
                emp['data_devolucao_prevista'],
                emp['data_devolucao_real'][:16] if emp['data_devolucao_real'] else '',
                emp['status']
            ), tags=tags)
        
        # Configurar tag de atrasado
        self.tree.tag_configure('atrasado', background='#ffcccc')
    
    def novo_emprestimo(self):
        FormularioEmprestimoUI(self.window, self.carregar_emprestimos)
    
    def devolver_livro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um empréstimo para registrar devolução!")
            return
        
        item = self.tree.item(selected[0])
        emprestimo_id = item['values'][0]
        status = item['values'][7]
        
        if status == 'devolvido':
            messagebox.showinfo("Info", "Este livro já foi devolvido!")
            return
        
        if messagebox.askyesno("Confirmar", "Deseja registrar a devolução deste livro?"):
            sucesso, mensagem = Emprestimo.devolver(emprestimo_id)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.carregar_emprestimos()
            else:
                messagebox.showerror("Erro", mensagem)
    
    def deletar_emprestimo(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um empréstimo para deletar!")
            return
        
        item = self.tree.item(selected[0])
        emprestimo_id = item['values'][0]
        
        if messagebox.askyesno("Confirmar", "Deseja realmente deletar este empréstimo?"):
            sucesso, mensagem = Emprestimo.deletar(emprestimo_id)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.carregar_emprestimos()
            else:
                messagebox.showerror("Erro", mensagem)


class FormularioEmprestimoUI:
    def __init__(self, parent, callback):
        self.window = tk.Toplevel(parent)
        self.callback = callback
        self.window.title("Novo Empréstimo")
        self.window.geometry("500x400")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.center_window()
        self.criar_widgets()
    
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
        
        # Usuário
        tk.Label(main_frame, text="Selecione o Usuário:", font=('Arial', 10)).pack(anchor='w')
        
        # Carregar usuários
        usuarios = Usuario.listar()
        self.usuarios_dict = {f"{u['nome_completo']} ({u['codigo_matricula']})": u['id'] 
                             for u in usuarios}
        
        self.combo_usuario = ttk.Combobox(main_frame, 
                                         values=list(self.usuarios_dict.keys()),
                                         state='readonly', font=('Arial', 10))
        self.combo_usuario.pack(fill='x', pady=(5, 20))
        
        # Livro
        tk.Label(main_frame, text="Selecione o Livro:", font=('Arial', 10)).pack(anchor='w')
        
        # Carregar livros disponíveis
        livros = Livro.listar()
        self.livros_dict = {f"{l['titulo']} - {l['autor']} (Disp: {l['quantidade_disponivel']})": l['id'] 
                           for l in livros if l['quantidade_disponivel'] > 0}
        
        self.combo_livro = ttk.Combobox(main_frame, 
                                       values=list(self.livros_dict.keys()),
                                       state='readonly', font=('Arial', 10))
        self.combo_livro.pack(fill='x', pady=(5, 20))
        
        # Dias de empréstimo
        tk.Label(main_frame, text="Dias de Empréstimo:", font=('Arial', 10)).pack(anchor='w')
        self.entry_dias = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_dias.insert(0, '14')
        self.entry_dias.pack(fill='x', pady=(5, 30))
        
        # Botões
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack()
        
        tk.Button(btn_frame, text="Realizar Empréstimo", command=self.salvar,
                 bg='#4CAF50', fg='white', font=('Arial', 10), 
                 padx=20, pady=8).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.window.destroy,
                 bg='#f44336', fg='white', font=('Arial', 10), 
                 padx=20, pady=8).pack(side='left', padx=5)
    
    def salvar(self):
        usuario_sel = self.combo_usuario.get()
        livro_sel = self.combo_livro.get()
        dias = self.entry_dias.get().strip()
        
        if not usuario_sel or not livro_sel:
            messagebox.showwarning("Atenção", "Selecione um usuário e um livro!")
            return
        
        try:
            dias = int(dias)
            if dias < 1:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Erro", "Dias de empréstimo deve ser um número válido!")
            return
        
        usuario_id = self.usuarios_dict[usuario_sel]
        livro_id = self.livros_dict[livro_sel]
        
        sucesso, mensagem = Emprestimo.criar(usuario_id, livro_id, dias)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.callback()
            self.window.destroy()
        else:
            messagebox.showerror("Erro", mensagem)
