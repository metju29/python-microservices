# DEV
`pip install --upgrade pip`
## Flask
1. `flask --app main run`
2. `flask --app main db init`
3. `flask --app main db migrate`
4. `flask --app main db upgrade`
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