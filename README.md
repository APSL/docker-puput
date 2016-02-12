[![Build Status](https://travis-ci.org/APSL/docker-puput.svg?branch=master)](https://travis-ci.org/APSL/docker-puput)

Minimal Usage
================
Consider to use docker-compose and our [docker-compose.yml example](https://github.com/APSL/docker-puput/blob/master/docker-compose.yml)

To test puput just clone the repository and:
```
$ docker-compose up -d
$ docker-compose ps
$ docker exec -ti dockerpuput_web_1 python manage.py migrate
$ docker exec -ti dockerpuput_web_1 python manage.py puput_initial_data
```
You can see the Puput blog at:
[http://localhost:8000/blog/](http://localhost:8000/blog/)

Docker Puput
========================

* All configuration via environment variables
* Docker compose example to test Puput quickly

Ports
=====

* 8000: puput

Env vars and default value:
=========
    DEBUG=False
    DATABASE_ENGINE=django.db.backends.mysql
    DATABASE_HOST=mysql
    DATABASE_NAME=puput
    DATABASE_USER=upuput
    DATABASE_PASSWORD=changeme
    ALLOWED_HOSTS="*"
    SECRET_KEY=alsochangeme_
