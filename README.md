# whosup

## Clone Repo
To get started, clone repo via 
`git clone https://github.com/codeformuskogee/whosup.git`

## Setup Env
Create a env.dev file in the same folder as your docker-compose.yml.

Sample:

```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=whosup_dev
SQL_USER=whosup
SQL_PASSWORD=whosup
SQL_HOST=db
SQL_PORT=5432
```

## Install Docker
Run `docker-compose build`
Then `docker-compose up`

## Run migrations
`docker-compose exec web python /usr/src/apps/manage.py migrate`

## Create Super User
`docker-compose exec web python /usr/src/apps/manage.py createsuperuser`

## Test Your App
Navigate to your dev url, e.g, http://127.0.0.1:8000
Login as admin: http://127.0.0.1:8000/admin