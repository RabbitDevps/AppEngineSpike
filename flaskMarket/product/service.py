from product.data import products_data
from product.model import Product


def get_products():
    return products_data

def get_product(product_id:str) -> list:
    products = products_data
    filter_ = filter(lambda product: product.code == product_id, products)
    return list(filter_)

def create_product(incoming_data:dict):
    new_product = Product(
         incoming_data.get("name")
        ,incoming_data.get("code")
        ,incoming_data.get("price")
        ,incoming_data.get("description")
    )
    products_data.append(new_product)

def delete_product(product_id:str) -> bool:
    lookup_product = Product("", product_id, 0, "")
    if lookup_product in products_data:
        products_data.remove(lookup_product)
        return True
    return False