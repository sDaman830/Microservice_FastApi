from typing import Union
from redis_om import get_redis_connection, HashModel
from fastapi import FastAPI

app = FastAPI()

redis = get_redis_connection(
    host = "redis-18749.c264.ap-south-1-1.ec2.cloud.redislabs.com",
    port=11844,
    password="uConh977IOeY6PtKJi5AV0DsSiwEAWav",
    decode_responses=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis
 
@app.get("/product")
def all():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

