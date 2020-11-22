from typing import Optional, Dict
from microservice import Product
import microservice
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, FastAPI
from fastapi.responses import Response

app = FastAPI()
router = APIRouter()


@app.get("/retrieve_productname_by_name")
def retrieve_productname_by_name(name: Optional[str] = None):
    products_filtered = microservice.retrieve_productname_by_name(name)
    return Response(content=products_filtered, media_type="application/json")


@app.get("/retrieve_product_by_name")
def retrieve_product_by_name(name: Optional[str] = None):
    products_filtered = microservice.retrieve_product_by_name(name)
    return Response(content=products_filtered, media_type="application/json")


@app.get("/retrieve_product_by_id")
def retrieve_product_by_id(_id: str):
    products_filtered = microservice.retrieve_product_by_id(_id)
    return Response(content=products_filtered, media_type="application/json")


@app.post("/retrieve_productname_by_options")
def retrieve_productname_by_options(options: Optional[Dict] = Body(None)):
    products_filtered = microservice.retrieve_productname_by_options(options)
    return Response(content=products_filtered, media_type="application/json")


@app.post("/create")
def create_product(product: Product = Body(..., example={
    "name": "Iphone11",
    "description": "Phone from Apple",
    "options": {"os": "Ios",
                "year": "2018"},
}, embed=True)):
    print(product)
    product = jsonable_encoder(product)
    print(product)
    new_product = microservice.create_product(product)
    return Response(content=new_product, media_type="application/json")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
