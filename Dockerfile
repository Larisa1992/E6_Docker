FROM python:3

RUN apt-get update
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./server.py /app/server.py
EXPOSE 8081

CMD ["python", "server.py"]