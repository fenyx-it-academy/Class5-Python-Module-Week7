"""
1. Create a `Product` class with attribute `name`, `brand` and `price`.
2. Add `toJson` method to `Product` class. The method should convert class object to JSON.
3. Create a `Brand` class with attirbute `name` and `year`.
4. Create a `Product` object and use `Brand` object for `brand` field.
4. Call `toJson` method."""
import json


class Product:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def tojson(self):
        self.dict = {"name": self.name, "brand": {
            "brand_name": self.brand.name, "brand_year": self.brand.year}, "price": self.price}
        with open(self.name+".json", "w") as jsonfile:
            json.dump(self.dict, jsonfile, indent=4)


class Brand:
    def __init__(self, name, year):
        self.name = name
        self.year = year


mercedes = Brand("c180", 2015)
car = Product("Car", mercedes, "500")

car.tojson()
