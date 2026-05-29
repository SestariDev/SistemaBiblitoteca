import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.livro import Livro

class LivrosUI:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Gerenciamento de Livros")
        self.window.geometry("1000x600")
        self.window.transient(parent)
        
        self.center_window()
        self.criar_widgets()
        self.carregar_livros()
    
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
        
        tk.Label(main_frame, text="Gerenciamento de Livros", 
                font=('Arial', 16, 'bold')).pack(pady=(0, 20))
        
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=(0, 10))
        
        tk.Button(btn_frame, text="Novo Livro", command=self.novo_livro,
                 bg='#4CAF50', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Editar", command=self.editar_livro,
                 bg='#2196F3', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Deletar", command=self.deletar_livro,
                 bg='#f44336', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Atualizar", command=self.carregar_livros,
                 bg='#FF9800', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        
        table_frame = tk.Frame(main_frame)
        table_frame.pack(expand=True, fill='both')
        
        scrollbar_y = ttk.Scrollbar(table_frame, orient='vertical')
        scrollbar_y.pack(side='right', fill='y')
        
        scrollbar_x = ttk.Scrollbar(table_frame, orient='horizontal')
        scrollbar_x.pack(side='bottom', fill='x')
        
        self.tree = ttk.Treeview(table_frame, 
                                 columns=('ID', 'Título', 'Autor', 'ISBN', 'Ano', 
                                         'Categoria', 'Total', 'Disponível'),
                                 show='headings',
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        self.tree.heading('ID', text='ID')
        self.tree.heading('Título', text='Título')
        self.tree.heading('Autor', text='Autor')
        self.tree.heading('ISBN', text='ISBN')
        self.tree.heading('Ano', text='Ano')
        self.tree.heading('Categoria', text='Categoria')
        self.tree.heading('Total', text='Total')
        self.tree.heading('Disponível', text='Disponível')
        
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Título', width=200)
        self.tree.column('Autor', width=150)
        self.tree.column('ISBN', width=120, anchor='center')
        self.tree.column('Ano', width=80, anchor='center')
        self.tree.column('Categoria', width=120)
        self.tree.column('Total', width=70, anchor='center')
        self.tree.column('Disponível', width=90, anchor='center')
        
        self.tree.pack(expand=True, fill='both')
        
        tk.Button(main_frame, text="Fechar", command=self.window.destroy,
                 font=('Arial', 10), padx=30, pady=8).pack(pady=(10, 0))
    
    def carregar_livros(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        livros = Livro.listar()
        for livro in livros:
            self.tree.insert('', 'end', values=(
                livro['id'],
                livro['titulo'],
                livro['autor'],
                livro['isbn'] or '',
                livro['ano_publicacao'] or '',
                livro['categoria'] or '',
                livro['quantidade_total'],
                livro['quantidade_disponivel']
            ))
    
    def novo_livro(self):
        FormularioLivroUI(self.window, None, self.carregar_livros)
    
    def editar_livro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um livro para editar!")
            return
        
        item = self.tree.item(selected[0])
        livro_id = item['values'][0]
        FormularioLivroUI(self.window, livro_id, self.carregar_livros)
    
    def deletar_livro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione um livro para deletar!")
            return
        
        item = self.tree.item(selected[0])
        livro_id = item['values'][0]
        titulo = item['values'][1]
        
        if messagebox.askyesno("Confirmar", f"Deseja realmente deletar o livro '{titulo}'?"):
            sucesso, mensagem = Livro.deletar(livro_id)
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.carregar_livros()
            else:
                messagebox.showerror("Erro", mensagem)


class FormularioLivroUI:
    def __init__(self, parent, livro_id, callback):
        self.window = tk.Toplevel(parent)
        self.livro_id = livro_id
        self.callback = callback
        self.window.title("Novo Livro" if not livro_id else "Editar Livro")
        self.window.geometry("500x500")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.center_window()
        self.criar_widgets()
        
        if livro_id:
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
        
        # Título
        tk.Label(main_frame, text="Título:", font=('Arial', 10)).pack(anchor='w')
        self.entry_titulo = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_titulo.pack(fill='x', pady=(5, 15))
        
        # Autor
        tk.Label(main_frame, text="Autor:", font=('Arial', 10)).pack(anchor='w')
        self.entry_autor = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_autor.pack(fill='x', pady=(5, 15))
        
        # ISBN
        tk.Label(main_frame, text="ISBN:", font=('Arial', 10)).pack(anchor='w')
        self.entry_isbn = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_isbn.pack(fill='x', pady=(5, 15))
        
        # Ano
        tk.Label(main_frame, text="Ano de Publicação:", font=('Arial', 10)).pack(anchor='w')
        self.entry_ano = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_ano.pack(fill='x', pady=(5, 15))
        
        # Categoria
        tk.Label(main_frame, text="Categoria:", font=('Arial', 10)).pack(anchor='w')
        self.entry_categoria = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_categoria.pack(fill='x', pady=(5, 15))
        
        # Quantidade
        tk.Label(main_frame, text="Quantidade Total:", font=('Arial', 10)).pack(anchor='w')
        self.entry_quantidade = tk.Entry(main_frame, font=('Arial', 10))
        self.entry_quantidade.insert(0, '1')
        self.entry_quantidade.pack(fill='x', pady=(5, 25))
        
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
        livro = Livro.buscar_por_id(self.livro_id)
        if livro:
            self.entry_titulo.insert(0, livro['titulo'])
            self.entry_autor.insert(0, livro['autor'])
            if livro['isbn']:
                self.entry_isbn.insert(0, livro['isbn'])
            if livro['ano_publicacao']:
                self.entry_ano.insert(0, str(livro['ano_publicacao']))
            if livro['categoria']:
                self.entry_categoria.insert(0, livro['categoria'])
            self.entry_quantidade.delete(0, tk.END)
            self.entry_quantidade.insert(0, str(livro['quantidade_total']))
    
    def salvar(self):
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        isbn = self.entry_isbn.get().strip()
        ano = self.entry_ano.get().strip()
        categoria = self.entry_categoria.get().strip()
        quantidade = self.entry_quantidade.get().strip()
        
        if not titulo or not autor:
            messagebox.showwarning("Atenção", "Título e autor são obrigatórios!")
            return
        
        try:
            ano = int(ano) if ano else None
            quantidade = int(quantidade)
            if quantidade < 1:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Erro", "Ano e quantidade devem ser números válidos!")
            return
        
        if self.livro_id:
            sucesso, mensagem = Livro.atualizar(self.livro_id, titulo, autor, isbn, 
                                               ano, categoria, quantidade)
        else:
            sucesso, mensagem = Livro.criar(titulo, autor, isbn, ano, categoria, quantidade)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.callback()
            self.window.destroy()
        else:
            messagebox.showerror("Erro", mensagem)
