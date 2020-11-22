from typing import Optional, Dict
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId, json_util, SON

cluster = MongoClient('localhost', 27017)
db = cluster['mservice']
collection = db['product']


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    options: Optional[Dict]


def create_product(product):
    print(product)
    product = collection.insert_one(product)
    new_product = collection.find_one({'_id': product.inserted_id})
    print(new_product)
    return json_util.dumps(new_product)


def retrieve_productname_by_name(name):
    if name:
        product = collection.find({"name": name})
    else:
        product = collection.find({})
    filtered_products = list(product)
    result = set()
    for product in filtered_products:
        result.add(product['name'])
    return json_util.dumps(result)


def retrieve_productname_by_options(options):
    product = collection.find(SON({"options": options}))
    filtered_products = list(product)
    result = set()
    for product in filtered_products:
        result.add(product['name'])
    return json_util.dumps(result)


def retrieve_product_by_id(_id):
    product = collection.find_one(SON({"_id": ObjectId(_id)}))
    print(product)
    return json_util.dumps(product)


def retrieve_product_by_name(name):
    if name:
        product = collection.find({"name": name})
    else:
        product = collection.find({})
    filtered_products = list(product)
    return json_util.dumps(filtered_products)
