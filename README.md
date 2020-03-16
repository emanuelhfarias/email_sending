<h1 align="center">
  <img src=".github/email.jpg" width="150px" />
</h1>

<h3 align="center">
  :email: Asynchronous email sending with Celery
</h3>

## Description
Simple django-admin dashboard to send asynchronous emails with Celery and Redis.

### Technologies
* Django
* Celery
* Redis

### Result
<h1 align="center">
  <img src=".github/result.png" width="800px" />
</h1>

### Running

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
