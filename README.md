# server-garagem
A ideia principal do projeto foi criar uma aplicação backend para atribuir
aos usuários cadastrados "garagens" e permitir que às garagens fossem adicionados "veículos".
Para tanto foram criadas duas aplicações usando django-rest-framework:
- user, para cadastro e autenticação de usuários 
- garage, para a gestão de garagens e veículos
Endpoints foram expostos para uso no projeto front-end, que pode ser acessado
pelo link: https://peaceful-jennings-026c64.netlify.app/

A modelagem dos dados está representadada na imagem model-database.
Todo o projeto pode ser executado localmente pelo comando docker-compose up 

