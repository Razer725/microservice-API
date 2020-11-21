from typing import Optional
import microservice
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body
from bson import ObjectId, json_util
from microservice import Product

app = FastAPI()
router = APIRouter()


@app.get("/retrieve_product")
def find_product(name: Optional[str],  options: Optional[list]):
    product = microservice.find_product()
    return product


@app.post("/create")
def create_product(product: Product = Body(..., example={
                "name": "Iphone11",
                "description": "Phone from Apple",
                "options": [
                    {"os": "Ios"},
                    {"year": "2018"}
                ],
            }, embed=True)):
    print(product)
    product = jsonable_encoder(product)
    print(product)
    new_product = microservice.create_product(product)
    return new_product


# @app.post("/create")
# def create_product(product: Product):
#     print(product)
#     product = json_util.loads(product)
#     print(product)
#     new_product = microservice.create_product(product)
#     return new_product


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
