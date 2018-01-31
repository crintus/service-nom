FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate --settings=config.settings && \
    ./manage.py collectstatic --noinput --settings=config.settings && \
    gunicorn --bind 0.0.0.0:$PORT --access-logfile - config.wsgi:application