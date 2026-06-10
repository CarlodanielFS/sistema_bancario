# sistema_bancario

# Sistema Bancário

Projeto desenvolvido em Python como parte do Bootcamp da DIO.

## Sobre o Projeto

O objetivo inicial deste desafio era refatorar o sistema bancário criado anteriormente, tornando o código mais organizado através da utilização de funções e da separação de responsabilidades.

Durante o desenvolvimento, aproveitei a oportunidade para estudar e aplicar conceitos do padrão de arquitetura MVC (Model-View-Controller), mesmo não sendo um requisito obrigatório do desafio.

A aplicação permite o cadastro de usuários, autenticação, gerenciamento de contas correntes e operações bancárias básicas por meio do terminal.

## Funcionalidades

- Cadastro de usuários
- Login com CPF e senha
- Criação de conta corrente
- Depósito
- Saque
- Consulta de extrato
- Encerramento do sistema

## Estrutura do Projeto

```text
sistema_bancario/
│
├── controller/
│   └── conta_controller.py
│
├── models/
│   └── conta_models.py
│
├── views/
│   └── conta_views.py
│
└── inicializar_sistema.py
```

### Controller

Responsável por controlar o fluxo do sistema, recebendo informações das Views e utilizando as regras de negócio presentes nos Models.

### Models

Responsável pelas regras de negócio e manipulação dos dados da aplicação.

### Views

Responsável pela interação com o usuário através do terminal, exibindo menus, mensagens e recebendo entradas de dados.

## Tecnologias Utilizadas

- Python
- Git
- GitHub
- MVC (Model-View-Controller)

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/CarlodanielFS/sistema_bancario.git
```

Acesse a pasta do projeto:

```bash
cd sistema_bancario
```

Execute o sistema:

```bash
python inicializar_sistema.py
```

O arquivo `inicializar_sistema.py` é o ponto de entrada da aplicação e responsável por iniciar todo o fluxo do sistema bancário.

## Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos como:

- Organização de código com funções
- Separação de responsabilidades
- Estrutura MVC
- Manipulação de listas e dicionários
- Controle de fluxo
- Modularização em Python
- Versionamento com Git e GitHub

## Autor

Carlos Daniel
