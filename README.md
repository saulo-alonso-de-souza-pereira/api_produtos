# API de Produtos e Entregas

Esta é uma API REST desenvolvida com Django e Django REST Framework para gerenciar produtos e entregas, com sistema de autenticação JWT e permissões baseadas em papéis.

## Como Rodar o Projeto

1.  Clone o repositório:
    `git clone https://github.com/saulo-alonso-de-souza-pereira/api_produtos.git`

2.  Navegue até a pasta do projeto:
    `cd api_produtos`

3.  Crie e ative um ambiente virtual:
    `python -m venv venv`
    `source venv/bin/activate`  # No Windows: `venv\Scripts\activate`

4.  Instale as dependências:
    `pip install -r requirements.txt`

5.  Execute as migrações do banco de dados:
    `python manage.py migrate`

6.  Crie um superusuário para acessar o painel Admin:
    `python manage.py createsuperuser`

7.  Inicie o servidor de desenvolvimento:
    `python manage.py runserver`

A API estará disponível em `http://127.0.0.1:8000/`.