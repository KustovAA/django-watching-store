### Как установить
* ```python -m venv env```
* ```source env/bin/activate```
* ```pip install -r requirements.txt```

### Как запускать
```
Необходимо создать файл .env в корне проекта.
```
```
В файле должны быть настройки подключения к базе данных:
```
* DB_ENGINE
* DB_HOST
* DB_PORT
* DB_NAME
* DB_USER
* DB_PASSWORD
```
И другие настройки:
```
* SECRET_KEY
* DEBUG
* ALLOWED_HOSTS
```
Команда для запуска:
```
* ```python manage.py runserver 0.0.0.0:8000```

