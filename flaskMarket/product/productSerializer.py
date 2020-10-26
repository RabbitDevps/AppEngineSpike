import json

from product.model import Product


class ProductSerializer(json.JSONEncoder):

    def default(self, object):
        if isinstance(object, Product):
            return object.__dict__
        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)


