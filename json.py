import json

class Brand():
    def __init__(self,b_n,b_y):
        self.b_n = b_n
        self.b_y = b_y

class Product(Brand):
    def __init__(self,b_n,b_y, name = None,price = None):
        super().__init__(b_n,b_y)
        self.name = name
        self.price = price
    def json(self):
        jsonStr = json.dumps(self.__dict__)
        return jsonStr

p = Product("Toshiba",2014)
print(p.json())