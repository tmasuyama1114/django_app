# django_app

docker-compose build --no-cache

docker-compose run web python3 manage.py makemigrations

docker-compose run web python3 manage.py migrate

docker-compose run web python3 manage.py createsuperuser

docker-compose up -d

-------./.env----------
DEBUG=1
SECRET_KEY=xxxxxxxxxxx
MYSQL_DATABASE=xxxxxx
MYSQL_USER=xxxx
MYSQL_PASSWORD=xxxx
