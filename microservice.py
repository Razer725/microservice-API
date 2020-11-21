from typing import Optional, List, Union
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId, json_util
from fastapi import Body

cluster = MongoClient('localhost', 27017)
db = cluster['mservice']
collection = db['product']


# class Options(BaseModel):
#     key: Optional[str]


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    options: Optional[list]


def create_product(product):
    print(product)
    product = collection.insert_one(product)
    new_product = collection.find_one({'_id': product.inserted_id})
    print(new_product)
    return json_util.dumps(new_product)


def find_product():
    product = collection.find_one({})
    print(product)
    return json_util.dumps(product)
