import json
from models.product import Product
class StorageManager:

    def __init__(self, filename="products.json"):
        self.filename = filename

    def save_products(self, products):
        data = []

        for product in products:
            data.append(product.dict_())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_products(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            products = []

            for item in data:
                product = Product(
                    item["category"],
                    item["name"],
                    item["id"],
                    item["price"],
                    
                    item["quantity"]
                )

                products.append(product)

            return products

        except FileNotFoundError:
            return []
