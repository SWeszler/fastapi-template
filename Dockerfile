FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
COPY ./start.sh /start.sh
RUN chmod +x /start.sh

RUN pip install -r requirements.txt

COPY . /app

ENV PORT=8080

CMD ["/start.sh"]