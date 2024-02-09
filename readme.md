<h1>Projeto: Gerenciador de Projetos

## Descrição do projeto 

<p align="justify">
 Este projeto consiste na criação de um Gerenciador de Projetos personalizado para a empresa Andrade Maia Advogados. Seu principal objetivo é proporcionar aos colaboradores uma plataforma eficiente para gerenciar projetos e atividades de forma centralizada. Para sua implementação, foi adotado o Framework Django para o desenvolvimento do back-end, garantindo a integridade e segurança das informações ao armazená-las diretamente em um banco de dados relacional. Essa abordagem possibilita a inclusão, modificação e exclusão de dados de maneira direta e simplificada através do próprio site."
</p>

## Funcionalidades

:heavy_check_mark: Modelagem de Banco de Dados

:heavy_check_mark: Gestão da administração do banco de dados relacional via Django

:heavy_check_mark: Gestão e administração de projetos e atividades vinculadas a esses projetos diretamente via site.

:heavy_check_mark: Inserção automatizada de informações no banco de dados relacional.

:heavy_check_mark: Dashboard contendo principais indicadores referente aos projetos na tela de index.


## Pré-requisitos

<dl>MySQL "https://dev.mysql.com/downloads/mysql/"</dl>
<dl>Python "https://www.python.org/downloads/"</dl>
<dl>Visual Studio Code "https://code.visualstudio.com/download"</dl>
<dl>NodeJS "https://nodejs.org/en/download"</dl>

## Bibliotecas/Frameworks

<dl>Bilioteca Chart.JS "Comando 'npm install chart.js'"</dl>
<dl>Framework Django "Comando 'pip install Django'"</dl>
<d1>Biblioteca Dotenv "Comando 'pip install python-dotenv'"</d1>

## Configuração do Banco de Dados e ambiente local da aplicação

1. **Instale os Pré-requisitos**

2. **Configuração do Ambiente MySQL**

3. **Configuração da Instância Local:** Configure uma instância local do MySQL. Anote as credenciais (nome de usuário, senha).

4. **Criação do Banco de Dados:** No MySQL, crie um banco de dados para o projeto.

5. **Clone o Repositório:** Faça o clone do seu repositório para sua máquina. 
    (git clone https://github.com/GuilhermeMoraes4/Project_Management).

6. **Crie o arquivo .env:** Na raiz do seu projeto, crie um arquivo chamado .env e configure as variáveis: database, senhadb, user.

7. **Configuração das Migracões:** Execute as migrações para criar as tabelas no banco de dados. 
    (python manage.y makemigrations, pip install migrate).

8. **Execução do Servidor Django:** Inicie o servidor Django. (python manage.py runserver).

## Como rodar os testes

1. **Acesse o Projeto:** Abra o navegador e acesse http://localhost:8000/  e faça o login para interagir com o projeto.

<div align="center">
<img src="https://github.com/GuilhermeMoraes4/Project_Management/blob/main/wiki_images/tela%20de%20login.jpg">


2. **Verifique o Dashboard:** Explore o dashboard na tela inicial, onde você poderá visualizar os principais indicadores referentes aos projetos.

<div align="center">
<img src="https://github.com/GuilhermeMoraes4/Project_Management/blob/main/wiki_images/Index_dashboard.jpg">

3. **Crie Projetos e Atividades:** Utilize a interface do site para criar e gerenciar projetos e atividades vinculadas.

<div align="center">
<img src="https://github.com/GuilhermeMoraes4/Project_Management/blob/main/wiki_images/Cadastre%20um%20projeto.jpg">

## Observação

:heavy_check_mark: Para versionamento do projeto no repositório privado foi utilizado GitFlow para todas as etapas do desenvolvimento, acredito que seja importante para boas práticas do desenvolvimento de software.

## Desenvolvedor :octocat:
<p>GuilhermeMoraes4</p>

