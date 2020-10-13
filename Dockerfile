FROM python:3.7-alpine

RUN mkdir /app
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
COPY ./server.py /app/server.py
EXPOSE 8081

CMD ["python", "server.py"]
