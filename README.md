# Sistema de Gerenciamento de Biblioteca 📚

**Projeto da disciplina Tópicos Especiais em Informática**  
**Fatec Ribeirão Preto - Análise e Desenvolvimento de Sistemas**

## 📋 Descrição do Projeto

Sistema completo de gerenciamento de biblioteca desenvolvido em Python com interface gráfica (Tkinter), permitindo:
- Cadastro e gerenciamento de usuários
- Cadastro e gerenciamento de livros
- Controle de empréstimos e devoluções
- Exportação de dados em formato JSON/ZIP
- Importação de dados de APIs públicas da web

## ✅ Requisitos Atendidos

### Interface Gráfica
- ✅ Mais de 10 interfaces gráficas implementadas:
  1. **Login** - Autenticação de usuários
  2. **Menu Principal** - Navegação do sistema
  3. **Sobre** - Informações do projeto e desenvolvedores
  4. **Lista de Usuários** - Visualização de usuários cadastrados
  5. **Formulário de Usuário** - Cadastro/edição de usuários
  6. **Lista de Livros** - Visualização do acervo
  7. **Formulário de Livro** - Cadastro/edição de livros
  8. **Lista de Empréstimos** - Visualização de empréstimos
  9. **Formulário de Empréstimo** - Registro de novos empréstimos
  10. **Exportar Dados** - Interface de exportação
  11. **Importar Dados** - Interface de importação com visualização

### Banco de Dados
- ✅ 4 tabelas implementadas (SQLite):
  1. **usuarios** - Cadastro de usuários do sistema
  2. **livros** - Cadastro do acervo de livros
  3. **emprestimos** - Controle de empréstimos
  4. **dados_importados** - Armazenamento de dados importados da web

- ✅ Operações CRUD implementadas para todas as tabelas:
  - **INSERT** - Criação de novos registros
  - **SELECT** - Listagem e busca de registros
  - **UPDATE** - Atualização de registros existentes
  - **DELETE** - Remoção de registros

### Funcionalidades Especiais
- ✅ **Exportação de Dados**: Todos os dados exportados em formato JSON e compactados em ZIP
- ✅ **Importação de Dados**: Dados importados de APIs públicas usando o módulo `requests`
  - API de Citações (quotable.io)
  - API de Fatos Aleatórios (uselessfacts.jsph.pl)
  - API de Atividades (boredapi.com)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado
- Acesso à internet (para importação de dados)

### Instalação

1. **Clone ou baixe o projeto**
   ```bash
   cd ProjetoSistemaBiblioteca
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema**
   ```bash
   python main.py
   ```

### Primeiro Acesso

O sistema já vem com um usuário administrador pré-cadastrado:
- **Matrícula**: `admin`
- **Senha**: `admin`

Use estas credenciais para fazer o primeiro login e depois cadastre novos usuários.

## 📁 Estrutura do Projeto

```
ProjetoSistemaBiblioteca/
├── main.py                 # Arquivo principal - executar este
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
│
├── database/              # Módulo de banco de dados
│   ├── db_config.py       # Configuração e criação do BD
│   └── biblioteca.db      # Banco de dados SQLite (gerado automaticamente)
│
├── models/                # Modelos de dados
│   ├── usuario.py         # CRUD de usuários
│   ├── livro.py          # CRUD de livros
│   └── emprestimo.py     # CRUD de empréstimos
│
├── ui/                    # Interfaces gráficas
│   ├── login.py          # Tela de login
│   ├── menu.py           # Menu principal
│   ├── sobre.py          # Tela sobre
│   ├── usuarios_ui.py    # Gerenciamento de usuários
│   ├── livros_ui.py      # Gerenciamento de livros
│   └── emprestimos_ui.py # Gerenciamento de empréstimos
│
└── utils/                 # Utilitários
    ├── export_data.py     # Exportação JSON/ZIP
    └── import_data.py     # Importação de dados da web
```

## 🎯 Funcionalidades Principais

### 1. Gerenciamento de Usuários
- Cadastrar novos usuários (alunos e administradores)
- Editar informações de usuários
- Excluir usuários
- Listar todos os usuários cadastrados

### 2. Gerenciamento de Livros
- Cadastrar novos livros no acervo
- Editar informações dos livros
- Excluir livros
- Controle de quantidade total e disponível
- Listar todo o acervo

### 3. Gerenciamento de Empréstimos
- Registrar novos empréstimos
- Definir prazo de devolução (padrão: 14 dias)
- Registrar devoluções
- Visualizar histórico de empréstimos
- Identificação visual de empréstimos atrasados

### 4. Exportação de Dados
- Exporta todos os dados do sistema
- Formato JSON com indentação
- Compactação automática em ZIP
- Inclui metadados da exportação

### 5. Importação de Dados da Web
- Importa citações de autores famosos
- Importa fatos aleatórios interessantes
- Importa sugestões de atividades
- Dados armazenados no banco de dados
- Visualização dos dados importados

## 👥 Desenvolvedores

**IMPORTANTE**: Edite o arquivo `ui/sobre.py` e atualize as informações dos desenvolvedores com seus dados reais:

```python
# Linha 52 do arquivo ui/sobre.py
dev_info = """
Nome: [SEU NOME COMPLETO]
Matrícula: [SEU CÓDIGO DE MATRÍCULA]

Nome: [NOME DO PARCEIRO (se em dupla)]
Matrícula: [MATRÍCULA DO PARCEIRO (se em dupla)]
"""
```

## 📊 Tecnologias Utilizadas

- **Python 3** - Linguagem principal
- **Tkinter** - Interface gráfica
- **SQLite3** - Banco de dados
- **Requests** - Requisições HTTP para importação de dados
- **JSON** - Formato de exportação de dados
- **Zipfile** - Compactação de arquivos

## 📝 Notas Importantes

1. O banco de dados é criado automaticamente na primeira execução
2. Todos os dados são armazenados localmente no arquivo `biblioteca.db`
3. As exportações são salvas no local escolhido pelo usuário
4. É necessária conexão com a internet apenas para importar dados da web
5. O sistema destaca visualmente empréstimos atrasados

## 🐛 Solução de Problemas

### Erro ao importar dados
- Verifique sua conexão com a internet
- As APIs públicas podem estar temporariamente indisponíveis
- Tente uma fonte de dados diferente

### Erro de permissão ao exportar
- Certifique-se de ter permissão de escrita na pasta escolhida
- Tente salvar em uma pasta diferente (ex: Documentos)

### Banco de dados não inicializa
- Verifique se tem permissão de escrita na pasta do projeto
- Exclua o arquivo `biblioteca.db` (se existir) e reinicie o sistema

## 📅 Informações da Entrega

- **Data de Entrega**: 22/05/2026
- **Data de Apresentação**: 29/05/2026
- **Valor**: 100% da nota da prova B2

## 📄 Licença

Este é um projeto acadêmico desenvolvido para fins educacionais.

---

**Centro Paula Souza**  
**Faculdade de Tecnologia de Ribeirão Preto**  
**Análise e Desenvolvimento de Sistemas**  
**Maio/2026**
