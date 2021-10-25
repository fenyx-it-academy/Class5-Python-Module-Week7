# # 3. To Json

# 1. Create a `Product` class with attribute `name`, `brand` and `price`.
# 2. Add `toJson` method to `Product` class. The method should convert class object to JSON.
# 3. Create a `Brand` class with attirbute `name` and `year`.
# 4. Create a `Product` object and use `Brand` object for `brand` field.
# 4. Call `toJson` method.
import json
class Brand:
    def __init__(self,b_name,b_year):
        self.b_year=b_year
        self.b_name=b_name
class Product(Brand):
    def __init__(self, name, b_name, price, b_year,):
        super().__init__(b_name, b_year)    
        self.name=name
        self.price=price
    def toJson(self):
        jsonStr = json.dumps(self.__dict__)
        return jsonStr

rotring=Product("Laptop",'Lenova','750',2020)
print(rotring.toJson())