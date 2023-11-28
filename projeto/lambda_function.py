import base64
import json
import logging
import os
import uuid
import boto3

import json
from decimal import Decimal
from facades.product_facade import ProductFacade
from product import Product
from product_service import ProductService
from repositories.product_dynamodb_repository import ProductDynamodbRepository
from repositories.product_s3_repository import ProductS3Repository

product_dynamodb_repository: ProductDynamodbRepository = ProductDynamodbRepository()
product_s3_repository: ProductS3Repository = ProductS3Repository()
product_service: ProductService = ProductService(
    product_dynamodb_repository, product_s3_repository)
product_facade: ProductFacade = ProductFacade(product_service)



def insert_handler(event, context):
    body = json.loads(event['body'])

    file_name = body["fileName"]
    product = {
        "Id": str(uuid.uuid4()),
        "Name": body["name"],
        "Rating": str(body["rating"]),
        "Author": body["author"],
        "Price": str(body["price"]),
        "FileName": file_name
    }
    
    base64_image = body.get('filebase64')
    if (base64_image):
        image = base64.b64decode(base64_image)
    
    
    product = Product(uuid.uuid4().hex, 
                      product.name, 
                      product.author, 
                      product.price, 
                      product.rating, 
                      product.file_name)
    
    product_facade.create(product, image)
    
    
def update_handler(event, context):
    body = json.loads(event['body'])
    
    id = body["id"]
    file_name = body["fileName"]
    product = {
        "Id": id,
        "Name": body["name"],
        "Rating": str(body["rating"]),
        "Author": body["author"],
        "Price": str(body["price"]),
        "FileName": file_name
    }
    
        
    base64_image = body.get('filebase64')
    if base64_image:
        image = base64.b64decode(base64_image)
        
       
    product = Product(id, 
                    product.name, 
                    product.author, 
                    product.price, 
                    product.rating, 
                    product.file_name)
    
    product_facade.update(id, product, image)

def delete_handler(event, context):
    body = json.loads(event['body'])
    
    product_id = body["Id"]

    product_facade.delete(product_id)    