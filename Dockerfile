FROM python:3.4
MAINTAINER Bernat bcabezas@apsl.net
#RUN apt-get update && apt-get install -y \
#    git mercurial \
#    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install uwsgi

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY conf/uwsgi.ini /uwsgi.ini

COPY . /app

WORKDIR /app
RUN python manage.py collectstatic  --noinput
#RUN python manage.py compress 

VOLUME /static
VOLUME /media

CMD ["uwsgi" , "--ini=/uwsgi.ini"]
EXPOSE 8000
#
