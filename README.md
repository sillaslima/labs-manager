Clonando o projeto

 $ git clone https://github.com/sillaslima/labs-manager.git
 $ cd labs-manager
 $ python3 -m venv .venv
 $ source .venv/bin/activate
 $ pip install -r requirements.txt
 $ python manage.py migrate
 $ python manage.py runserver

 Executando o app do Admin:
 http://localhost:8000/admin/
 Username:
 admin
 Password:
 admin@123
 
 Link da APP http://localhost:8000/admin/coreManagerEmployees/ 

Rodando os testes.
$ npm install -g newman
$ newman run labs.postman_collection.json
