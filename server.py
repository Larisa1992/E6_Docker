from bottle import route, run, request, HTTPError
from pymemcache.client.base import Client
import json
import os

MEMCACHED_HOST = os.environ.get('MEMCACHED_HOST')

def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2

def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode("utf-8")
    if flags == 2:
        return json.loads(value.decode("utf-8"))
    # raise Exception("Unknown serialization format")

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

@route("/fib/<k:int>")
def fib_handler(k):
    client = Client((MEMCACHED_HOST, '11211')
        , serializer=json_serializer
        , deserializer=json_deserializer) # клиент кэширования
    fib_result = client.get(str(k)) # число фибоначчи из кэша
    if fib_result is None:
        result = fib(k)
        client.set(str(k), result)  # кэшируем число фибоначчи
    else: 
        result = fib_result
    print('fib_result=', fib_result)
    return str(result)

# client = Client(('localhost', 8080))
# client.set(k, fib_handler(k))
# fib_result = client.get('some_key')
# print(fib_result)


if __name__ == "__main__":
    run(host="0.0.0.0", port=8081)
