
class Product:

    def __init__(self, name:str, code:str, price:float, description:str):
        self.name = name
        self.code = code
        self.price = price
        self.description = description

    def __repr__(self):
        return f"{self.name} {self.code} {self.price} {self.description}"

    def __str__(self):
        return f"{self.name} {self.code} {self.price} {self.description}"

    def __eq__(self, other):
        return self.code == other.code