FROM python:alpine3.7
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./server.py /app/server.py
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["server.py"]