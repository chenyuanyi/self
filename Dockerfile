FROM zeromake/base-uwsgi:0.1

COPY server/requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /data/web/

ENV CONFIG_FILE /data/web/conf/conf.json

WORKDIR /data/web/

CMD ["uwsgi", "--ini", "/data/web/uwsgi.ini"]