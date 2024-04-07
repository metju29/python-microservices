# DEV
`pip install --upgrade pip`
## Django
1. `pip install django`
2. `pip install djangorestframework`
3. `django-admin startproject admin .`
4. `python3 manage.py runserver`
5. `python3 manage.py startapp products`
6. `python3 manage.py makemigrations`
7. ` python3 manage.py makemigrations`
## Docker
1. `docker-compose up`
2. `docker-compose exec backend sh`
3. `docker-compose up --build`
4. `docker-compose up -d db`
## DBeaver
To connect to the database via DBeaver:
1. Right-click your connection, choose "Edit Connection"
2. On the "Connection settings" screen (main screen), click on "Edit Driver Settings"
3. Click on "Driver properties"
4. Set these two properties: "allowPublicKeyRetrieval" to `true` and "useSSL" to `false`