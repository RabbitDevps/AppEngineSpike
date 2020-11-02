import unittest
import product.service as product_service


class AssetManagerTest(unittest.TestCase):

    def test_find_product(self):
        products = product_service.get_product("001")
        for p in products:
            self.assertEqual('001', p.code)

    def test_create_product(self):
        data = {
              "name": "Noodles"
            , "code": "004"
            , "price": 123
            , "description": "Italian pasta"
        }
        product_service.create_product(data)
        products = product_service.get_product("004")
        for p in products:
            self.assertEqual('004', p.code)
            self.assertEqual('Noodles', p.name)

    def test_delete_product(self):
        product_id = "001"
        product_service.delete_product(product_id)
        products = product_service.get_product("001")
        self.assertFalse(products)
