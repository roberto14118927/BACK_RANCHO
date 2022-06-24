FROM python:3.10.5-alpine3.16

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN  apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev  jpeg-dev zlib-dev \
  && pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "sh", "entrypoint.sh" ]
