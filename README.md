Clonando o projeto

 git clone https://github.com/labs-manager/labs-manager.git
 cd labs-manager
 python3 -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt
 python manage.py migrate
 python manage.py runserver

Rodando os testes.

npm install -g newman
newman run labs.postman_collection.json