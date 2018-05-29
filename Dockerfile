FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /app/requirements

RUN pip install --upgrade pip
RUN pip install -r /app/requirements/local.txt

COPY ./runserver.sh /runserver.sh
RUN sed -i 's/\r//' /runserver.sh

RUN chmod +x /runserver.sh