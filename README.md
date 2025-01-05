# Projeto Cadastro de Usuários 📝

Este projeto é uma aplicação para cadastro de usuários, desenvolvida utilizando o framework Django. A aplicação permite gerenciar usuários através de funcionalidades como cadastro, exclusão e listagem de usuários.

## Funcionalidades 🚀

- **Cadastro de novos usuários**: Permite adicionar novos usuários ao sistema.
- **Exclusão de usuários**: Permite remover usuários existentes do sistema.
- **Listagem de usuários**: Exibe uma lista de todos os usuários cadastrados no sistema.

## Tecnologias Utilizadas 🛠️

- **Linguagem de Programação**: Python 🐍
- **Framework**: Django 🌐

## Como Executar o Projeto 🏃‍♂️

1. **Clone o repositório**:
  ```bash
  git clone https://github.com/MonicaAlvesP/cadastre-me.git
  ```
2. **Navegue até o diretório do projeto**:
  ```bash
  cd projeto_cad_usuarios
  ```
3. **Crie um ambiente virtual**:
  ```bash
  python -m venv venv
  ```
4. **Ative o ambiente virtual**:
  - No Windows:
    ```bash
    venv\Scripts\activate
    ```
  - No Linux/Mac:
    ```bash
    source venv/bin/activate
    ```
5. **Instale as dependências**:
  ```bash
  pip install -r requirements.txt
  ```
6. **Realize as migrações do banco de dados**:
  ```bash
  python manage.py migrate
  ```
7. **Inicie o servidor de desenvolvimento**:
  ```bash
  python manage.py runserver
  ```

Agora você pode acessar a aplicação no seu navegador através do endereço `http://127.0.0.1:8000/`. 🌍
