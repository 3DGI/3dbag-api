FROM tiangolo/uwsgi-nginx-flask:python3.8
ENV LISTEN_PORT 3200
EXPOSE 3200
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/3dbag-api/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

