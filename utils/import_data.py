import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_config import get_connection

class ImportarDadosUI:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Importar Dados da Web")
        self.window.geometry("800x600")
        self.window.transient(parent)
        
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
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        tk.Label(main_frame, text="Importar Dados da Web", 
                font=('Arial', 16, 'bold')).pack(pady=(0, 20))
        
        # Instruções
        info_text = """Esta funcionalidade permite importar dados de APIs públicas da web.
Os dados importados serão armazenados no banco de dados e exibidos abaixo."""
        
        tk.Label(main_frame, text=info_text, font=('Arial', 9), 
                justify='left', fg='gray').pack(anchor='w', pady=(0, 15))
        
        # Frame de opções
        options_frame = tk.Frame(main_frame)
        options_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(options_frame, text="Escolha uma fonte de dados:", 
                font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0, 10))
        
        # Botões de importação
        btn_frame = tk.Frame(options_frame)
        btn_frame.pack(fill='x')
        
        tk.Button(btn_frame, text="📚 Importar Citações (Quotes)", 
                 command=lambda: self.importar_dados('quotes'),
                 bg='#4CAF50', fg='white', font=('Arial', 9),
                 width=25).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="📖 Importar Fatos Aleatórios", 
                 command=lambda: self.importar_dados('facts'),
                 bg='#2196F3', fg='white', font=('Arial', 9),
                 width=25).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🌐 Importar Atividades", 
                 command=lambda: self.importar_dados('activities'),
                 bg='#FF9800', fg='white', font=('Arial', 9),
                 width=25).pack(side='left', padx=5)
        
        # Separador
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=15)
        
        # Área de resultados
        tk.Label(main_frame, text="Dados Importados:", 
                font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0, 5))
        
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
                                 columns=('ID', 'Título', 'Conteúdo', 'Fonte', 'Data'),
                                 show='headings',
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        self.tree.heading('ID', text='ID')
        self.tree.heading('Título', text='Título')
        self.tree.heading('Conteúdo', text='Conteúdo')
        self.tree.heading('Fonte', text='Fonte')
        self.tree.heading('Data', text='Data Importação')
        
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Título', width=150)
        self.tree.column('Conteúdo', width=300)
        self.tree.column('Fonte', width=120, anchor='center')
        self.tree.column('Data', width=150, anchor='center')
        
        self.tree.pack(expand=True, fill='both')
        
        # Botões inferiores
        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(fill='x', pady=(10, 0))
        
        tk.Button(bottom_frame, text="🔄 Atualizar Lista", 
                 command=self.carregar_dados_importados,
                 font=('Arial', 9)).pack(side='left', padx=5)
        
        tk.Button(bottom_frame, text="Fechar", 
                 command=self.window.destroy,
                 font=('Arial', 9), padx=20).pack(side='right')
        
        # Carregar dados existentes
        self.carregar_dados_importados()
    
    def importar_dados(self, tipo):
        """Importa dados de APIs públicas"""
        try:
            if tipo == 'quotes':
                # API de citações
                url = 'https://api.quotable.io/random'
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                
                titulo = f"Citação de {data.get('author', 'Desconhecido')}"
                conteudo = data.get('content', '')
                fonte = 'quotable.io'
                
            elif tipo == 'facts':
                # API de fatos aleatórios
                url = 'https://uselessfacts.jsph.pl/random.json?language=en'
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                
                titulo = "Fato Aleatório"
                conteudo = data.get('text', '')
                fonte = 'uselessfacts.jsph.pl'
                
            elif tipo == 'activities':
                # API de atividades
                url = 'https://www.boredapi.com/api/activity'
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                
                titulo = f"Atividade - {data.get('type', 'geral')}"
                conteudo = data.get('activity', '')
                fonte = 'boredapi.com'
            
            else:
                raise ValueError("Tipo de importação inválido")
            
            # Salvar no banco de dados
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO dados_importados (titulo, conteudo, fonte)
                VALUES (?, ?, ?)
            ''', (titulo, conteudo, fonte))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Sucesso", f"Dados importados com sucesso de {fonte}!")
            self.carregar_dados_importados()
            
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro de Conexão", 
                               f"Erro ao conectar com a API:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao importar dados:\n{str(e)}")
    
    def carregar_dados_importados(self):
        """Carrega e exibe dados importados"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Carregar dados
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dados_importados ORDER BY data_importacao DESC')
        dados = cursor.fetchall()
        conn.close()
        
        for dado in dados:
            # Limitar tamanho do conteúdo exibido
            conteudo = dado['conteudo']
            if len(conteudo) > 100:
                conteudo = conteudo[:97] + '...'
            
            self.tree.insert('', 'end', values=(
                dado['id'],
                dado['titulo'],
                conteudo,
                dado['fonte'],
                dado['data_importacao'][:16] if dado['data_importacao'] else ''
            ))
