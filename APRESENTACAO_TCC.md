# Guia para Apresentação de TCC - Sistema de Gerenciamento de Biblioteca

## Informações do Projeto

### Dados Acadêmicos
- **Disciplina**: Tópicos Especiais em Informática
- **Instituição**: Fatec Ribeirão Preto - ADS (Análise e Desenvolvimento de Sistemas)
- **Tema**: Sistema de Gerenciamento de Biblioteca
- **Período**: Maio/2026
- **Versão**: 1.0

### Objetivo do Projeto
Desenvolver uma aplicação desktop em Python para gerenciar o acervo de uma biblioteca, incluindo cadastro de livros, usuários e controle de empréstimos, com interface gráfica intuitiva e funcionalidades de importação/exportação de dados.

---

## Estrutura da Apresentação

### 1. INTRODUÇÃO (2-3 slides)
**Conteúdo sugerido:**
- Apresentação do tema
- Justificativa: Por que um sistema de biblioteca é importante?
- Contexto: Necessidade de digitalização e automação em bibliotecas
- Objetivo geral do projeto

**Pontos-chave:**
- Facilitar o gerenciamento de acervos bibliográficos
- Reduzir processos manuais e erros humanos
- Fornecer controle eficiente de empréstimos e devoluções
- Interface amigável para diferentes perfis de usuários

### 2. FUNDAMENTAÇÃO TEÓRICA (2-3 slides)
**Tecnologias Utilizadas:**
- **Linguagem**: Python 3.x
  - Justificativa: Linguagem versátil, de fácil aprendizado e com ampla biblioteca de recursos
- **Interface Gráfica**: Tkinter
  - Justificativa: Biblioteca padrão do Python, multiplataforma e sem dependências externas
- **Banco de Dados**: SQLite
  - Justificativa: Leve, embutido, sem necessidade de servidor dedicado
- **Formato de Dados**: JSON/ZIP
  - Justificativa: Portabilidade e facilidade de integração

**Conceitos Aplicados:**
- Programação Orientada a Objetos (POO)
- Padrão MVC (Model-View-Controller) adaptado
- Persistência de dados com SQLite
- Interface gráfica com eventos
- Validação de dados e tratamento de exceções

### 3. REQUISITOS DO SISTEMA (1-2 slides)

#### Requisitos Funcionais:
- **RF01**: Cadastrar, editar, listar e excluir livros
- **RF02**: Cadastrar, editar, listar e excluir usuários
- **RF03**: Registrar empréstimos de livros
- **RF04**: Registrar devoluções de livros
- **RF05**: Listar empréstimos ativos e histórico
- **RF06**: Exportar dados em formato JSON/ZIP
- **RF07**: Importar dados de fontes externas (web)
- **RF08**: Sistema de autenticação de usuários
- **RF09**: Exibir informações do sistema

#### Requisitos Não Funcionais:
- **RNF01**: Interface intuitiva e responsiva
- **RNF02**: Persistência local de dados (SQLite)
- **RNF03**: Segurança no acesso (login)
- **RNF04**: Portabilidade (Windows, Linux, macOS)
- **RNF05**: Performance adequada para bibliotecas de pequeno/médio porte

### 4. ARQUITETURA DO SISTEMA (2-3 slides)

#### Estrutura de Diretórios:
```
ProjetoSistemaBiblioteca/
├── main.py                 # Ponto de entrada da aplicação
├── iniciar.bat            # Script de inicialização
├── requirements.txt       # Dependências do projeto
├── database/
│   └── db_config.py      # Configuração e inicialização do BD
├── models/
│   ├── livro.py          # Modelo de dados: Livro
│   ├── usuario.py        # Modelo de dados: Usuário
│   └── emprestimo.py     # Modelo de dados: Empréstimo
├── ui/
│   ├── login.py          # Interface de login
│   ├── menu.py           # Menu principal
│   ├── livros_ui.py      # Gerenciamento de livros
│   ├── emprestimos_ui.py # Gerenciamento de empréstimos
│   └── sobre.py          # Informações do sistema
└── utils/
    ├── usuarios_ui.py    # Gerenciamento de usuários
    ├── export_data.py    # Exportação de dados
    └── import_data.py    # Importação de dados
```

#### Camadas da Aplicação:
1. **Camada de Apresentação (UI)**: Interfaces gráficas com Tkinter
2. **Camada de Negócio (Models)**: Lógica de negócio e regras
3. **Camada de Dados (Database)**: Persistência e acesso ao SQLite
4. **Camada de Utilitários (Utils)**: Funcionalidades auxiliares

### 5. FUNCIONALIDADES PRINCIPAIS (3-4 slides)

#### 5.1 Gerenciamento de Livros
**Características:**
- Cadastro completo: título, autor, editora, ano, ISBN, categoria
- Listagem com busca e filtros
- Edição de informações
- Exclusão com validação (verifica empréstimos ativos)
- Interface tabular com scroll

**Demonstração sugerida:**
- Screenshot da tela de cadastro
- Screenshot da listagem de livros
- Fluxo: Adicionar → Editar → Visualizar

#### 5.2 Gerenciamento de Usuários
**Características:**
- Cadastro: nome completo, CPF, email, telefone, endereço
- Tipos de usuário: administrador, bibliotecário, leitor
- Validação de CPF e email
- Listagem e busca
- Controle de permissões

**Demonstração sugerida:**
- Screenshot do formulário de cadastro
- Diferentes níveis de acesso
- Fluxo de autenticação

#### 5.3 Controle de Empréstimos
**Características:**
- Registro de empréstimo: usuário + livro + data
- Cálculo automático de data de devolução
- Registro de devolução
- Visualização de empréstimos ativos
- Histórico completo de movimentações
- Validações: livro disponível, limite de empréstimos por usuário

**Demonstração sugerida:**
- Screenshot da tela de empréstimos
- Fluxo: Emprestar → Consultar → Devolver
- Tratamento de atrasos

#### 5.4 Importação e Exportação
**Características:**
- **Exportação**: Gera arquivo ZIP com JSON dos dados
- **Importação**: Busca dados de APIs externas (simulação)
- Backup e restauração de dados
- Integração com fontes externas

**Demonstração sugerida:**
- Processo de exportação
- Estrutura dos arquivos JSON
- Casos de uso: backup, migração

### 6. BANCO DE DADOS (1-2 slides)

#### Modelo de Dados (Entidades principais):

**Tabela: livros**
- id (PK)
- titulo
- autor
- editora
- ano_publicacao
- isbn
- categoria
- quantidade_total
- quantidade_disponivel

**Tabela: usuarios**
- id (PK)
- nome_completo
- cpf (unique)
- email
- telefone
- endereco
- tipo_usuario
- senha (hash)

**Tabela: emprestimos**
- id (PK)
- livro_id (FK)
- usuario_id (FK)
- data_emprestimo
- data_devolucao_prevista
- data_devolucao_real
- status (ativo/devolvido)

#### Relacionamentos:
- Um usuário pode ter múltiplos empréstimos (1:N)
- Um livro pode ter múltiplos empréstimos ao longo do tempo (1:N)
- Empréstimo relaciona usuário e livro (N:N através de tabela associativa)

### 7. INTERFACE DO USUÁRIO (2-3 slides)

#### Características da Interface:
- Design limpo e profissional
- Cores consistentes (tema azul predominante)
- Botões com cores intuitivas:
  - Verde: Adicionar/Novo
  - Azul: Editar/Ações principais
  - Vermelho: Deletar/Cancelar
  - Laranja: Atualizar
- Centralização automática de janelas
- Validação em tempo real
- Mensagens de feedback claras

#### Fluxo de Navegação:
1. **Login** → Autenticação
2. **Menu Principal** → Hub de funcionalidades
3. **Módulos específicos** → Livros, Usuários, Empréstimos
4. **Ações** → CRUD completo em cada módulo
5. **Utilitários** → Importar/Exportar/Sobre

**Demonstração sugerida:**
- Screenshots de cada tela principal
- Navegação entre módulos
- Tratamento de erros (validações)

### 8. TESTES E VALIDAÇÕES (1-2 slides)

#### Tipos de Teste Realizados:
- **Testes Funcionais**: Cada funcionalidade foi testada individualmente
- **Testes de Integração**: Fluxo completo (cadastro → empréstimo → devolução)
- **Testes de Validação**: CPF, email, datas, campos obrigatórios
- **Testes de Interface**: Usabilidade e responsividade

#### Cenários de Teste:
- Cadastro de livro com dados válidos/inválidos
- Tentativa de emprestar livro indisponível
- Devolução de livro dentro/fora do prazo
- Exclusão de registro com dependências
- Importação/Exportação de dados

#### Resultados:
- Sistema estável e funcional
- Validações eficazes
- Interface responsiva
- Performance adequada

### 9. DESAFIOS E SOLUÇÕES (1-2 slides)

#### Desafios Encontrados:
1. **Desafio**: Gerenciamento de estados das janelas Tkinter
   - **Solução**: Uso de Toplevel e transient para hierarquia de janelas

2. **Desafio**: Validação de CPF e dados
   - **Solução**: Implementação de funções de validação customizadas

3. **Desafio**: Organização do código
   - **Solução**: Separação em camadas (MVC adaptado)

4. **Desafio**: Consistência de dados (empréstimos vs disponibilidade)
   - **Solução**: Transações atômicas e validações em cascata

5. **Desafio**: Interface responsiva com tabelas grandes
   - **Solução**: Implementação de scrollbars e paginação virtual

### 10. RESULTADOS OBTIDOS (1 slide)

#### Objetivos Alcançados:
✓ Sistema funcional e completo  
✓ Interface intuitiva e amigável  
✓ Todas as funcionalidades implementadas  
✓ Banco de dados estruturado e normalizado  
✓ Código organizado e documentado  
✓ Sistema portátil e fácil de instalar  
✓ Backup e restauração de dados  

#### Métricas:
- **Linhas de código**: ~2000+ linhas
- **Módulos**: 12 arquivos Python
- **Funcionalidades**: 9 principais
- **Telas**: 7 interfaces distintas

### 11. DEMONSTRAÇÃO PRÁTICA (Durante apresentação)

#### Roteiro Sugerido para Demo:
1. **Login** (5-10 segundos)
   - Mostrar tela de login
   - Realizar autenticação

2. **Cadastrar Livro** (20-30 segundos)
   - Abrir módulo de livros
   - Adicionar novo livro com dados reais
   - Salvar e visualizar na lista

3. **Cadastrar Usuário** (15-20 segundos)
   - Abrir módulo de usuários
   - Cadastrar um leitor
   - Mostrar validação de CPF

4. **Realizar Empréstimo** (20-30 segundos)
   - Abrir módulo de empréstimos
   - Selecionar usuário e livro
   - Registrar empréstimo
   - Mostrar atualização de disponibilidade

5. **Exportar Dados** (10-15 segundos)
   - Exportar para JSON/ZIP
   - Mostrar arquivo gerado

**Tempo total da demo**: 1-2 minutos

### 12. TRABALHOS FUTUROS (1 slide)

#### Melhorias Propostas:
- **Funcionalidades**:
  - Sistema de multas por atraso
  - Reserva de livros
  - Geração de relatórios em PDF
  - Dashboard com estatísticas
  - Sistema de notificações (email/SMS)
  - Busca avançada com filtros múltiplos

- **Técnicas**:
  - Migração para PostgreSQL (ambiente multiusuário)
  - API REST para integração web/mobile
  - Interface web com Flask/Django
  - Aplicativo móvel
  - Sistema de logs detalhado
  - Implementação de testes automatizados

- **UX/UI**:
  - Modo escuro
  - Temas personalizáveis
  - Suporte a internacionalização (i18n)
  - Acessibilidade aprimorada

### 13. CONCLUSÃO (1 slide)

#### Resumo:
O Sistema de Gerenciamento de Biblioteca atende plenamente aos objetivos propostos, oferecendo uma solução completa e eficiente para automação de processos bibliotecários. A aplicação demonstra a viabilidade de desenvolvimento de sistemas desktop com Python e Tkinter, proporcionando interface amigável e funcionalidades robustas.

#### Aprendizados:
- Desenvolvimento de aplicações desktop com Python
- Implementação de padrões de projeto
- Gerenciamento de banco de dados relacional
- Criação de interfaces gráficas com Tkinter
- Trabalho com arquitetura em camadas
- Boas práticas de programação e documentação

#### Contribuições:
- Solução prática para bibliotecas de pequeno/médio porte
- Código aberto e documentado para fins educacionais
- Base para projetos mais complexos na área

---

## Recursos Visuais para Apresentação

### Screenshots Essenciais:
1. ✅ Tela de Login
2. ✅ Menu Principal
3. ✅ Listagem de Livros (com dados)
4. ✅ Formulário de Cadastro de Livro
5. ✅ Listagem de Usuários
6. ✅ Tela de Empréstimos (tabela preenchida)
7. ✅ Formulário de Novo Empréstimo
8. ✅ Tela "Sobre" com informações do projeto
9. ✅ Exemplo de arquivo exportado (JSON)
10. ✅ Diagrama da arquitetura do sistema

### Diagramas Recomendados:
1. **Diagrama de Casos de Uso**: Atores e funcionalidades
2. **Diagrama de Classes**: Models e relacionamentos
3. **Diagrama ER**: Estrutura do banco de dados
4. **Fluxograma**: Processo de empréstimo
5. **Arquitetura do Sistema**: Camadas e componentes

---

## Dicas para Apresentação

### Preparação:
- Ensaiar a apresentação 2-3 vezes
- Testar o sistema antes da apresentação
- Ter dados de exemplo prontos no banco
- Preparar backup em caso de problemas técnicos
- Cronometrar para não ultrapassar o tempo

### Durante a Apresentação:
- Falar claramente e em ritmo adequado
- Fazer contato visual com a banca
- Demonstrar segurança sobre o projeto
- Antecipar possíveis perguntas
- Ser objetivo nas explicações técnicas

### Possíveis Perguntas da Banca:
1. Por que escolheu Python e Tkinter?
2. Como o sistema lida com concorrência (múltiplos usuários)?
3. Quais validações foram implementadas?
4. Como funciona a segurança (autenticação)?
5. O sistema é escalável para grandes bibliotecas?
6. Quais foram os maiores desafios técnicos?
7. Como foi o processo de testes?
8. Há tratamento de exceções e erros?

### Respostas Preparadas:
- **Escalabilidade**: Sistema projetado para pequeno/médio porte. Para grandes volumes, seria necessário migrar para PostgreSQL e arquitetura cliente-servidor
- **Segurança**: Implementado sistema de autenticação básico. Em produção, seria necessário hash de senhas (bcrypt) e controle de sessões
- **Testes**: Realizados testes manuais de cada funcionalidade. Próximo passo seria implementar testes automatizados (pytest)
- **Concorrência**: SQLite possui limitações para acesso concorrente. Sistema atual é monousuário/desktop

---

## Checklist Final

### Antes da Apresentação:
- [ ] Slides preparados e revisados
- [ ] Sistema testado e funcionando
- [ ] Banco de dados com exemplos realistas
- [ ] Screenshots em alta qualidade
- [ ] Diagramas claros e legíveis
- [ ] Código fonte documentado
- [ ] Backup do projeto
- [ ] Cronometragem dentro do tempo

### Conteúdo dos Slides:
- [ ] Introdução e contexto
- [ ] Objetivos claros
- [ ] Fundamentação teórica
- [ ] Requisitos do sistema
- [ ] Arquitetura e tecnologias
- [ ] Funcionalidades principais
- [ ] Demonstração/Screenshots
- [ ] Resultados e testes
- [ ] Conclusão
- [ ] Trabalhos futuros

### Entregáveis:
- [ ] Apresentação em PDF/PowerPoint
- [ ] Código fonte
- [ ] Documentação técnica (README.md)
- [ ] Este guia de apresentação
- [ ] Diagramas em formato editável
- [ ] Manual do usuário (se solicitado)

---

## Informações Técnicas para Referência

### Dependências (requirements.txt):
```
# Sem dependências externas - apenas bibliotecas padrão do Python
# tkinter (incluído no Python)
# sqlite3 (incluído no Python)
```

### Como Executar:
```bash
# Windows
iniciar.bat

# Ou diretamente:
python main.py
# ou
py -3 main.py
```

### Estrutura do Banco de Dados:
- **Arquivo**: `biblioteca.db` (criado automaticamente)
- **Localização**: Raiz do projeto
- **Tipo**: SQLite 3
- **Tabelas**: livros, usuarios, emprestimos

### Contato e Informações:
- **Repositório**: [Adicionar link se houver]
- **Documentação**: README.md
- **Licença**: [Definir se aplicável]

---

## Conclusão do Guia

Este documento fornece uma estrutura completa para criar uma apresentação profissional de TCC sobre o Sistema de Gerenciamento de Biblioteca. Adapte o conteúdo conforme as especificações da sua instituição e o tempo disponível para apresentação.

**Tempo sugerido**: 15-20 minutos de apresentação + 5-10 minutos de perguntas

**Boa sorte na apresentação! 🎓**
