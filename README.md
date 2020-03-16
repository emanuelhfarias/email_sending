
Requirements
Docker
docker-compose (pip install docker-compose)

```
./manage.py migrate
./manage.py createsuperuser
docker run -it -p 6379:6379 redis
docker run -it -p 1025:1025 -p 8025:8025 mailhog/mailhog
celery -A core worker -l info
```
