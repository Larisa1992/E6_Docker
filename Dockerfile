FROM python:3

RUN apt update
RUN apt-get install memcached
RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./server.py /app/server.py
EXPOSE 8081

CMD ["python", "server.py"]