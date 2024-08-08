FROM python:3.10-alpine

RUN mkdir /www
WORKDIR /www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libpq \
    # pillow dependencies
    jpeg-dev \
    zlib-dev \
    # pycurl dependencies
    curl-dev

COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]

RUN mkdir /requirements
COPY ./requirements/ ./requirements
RUN pip install --upgrade pip
RUN pip3 install -r ./requirements/dev.txt

COPY . /www/
