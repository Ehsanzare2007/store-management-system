class Product:
    def __init__(self,category,name,id,price,quantity):
        self.id=int(id)
        self.name=name
        self.price=float(price)
        self.quantity=int(quantity)
        self.category=category
    def dict_(self):
        dict_={
        "category":self.category,
        'name':self.name,
        'id':self.id,
        'price':self.price,
        'quantity':self.quantity
        }
        return dict_
    @classmethod
    def add_product(cls):
        name=input('Enter product name:').strip()
        id=input('Enter product id:')
        while not id.isdigit():
            id=input('Enter product id:')
        id=int(id)
        while True:
            price=input('Enter product price: ')
            try:
                price=float(price)
                break
            except ValueError:
                print(" Invalid input! Please enter a number (e.g., 19.99)")
            
        quantity=input("Enter product quantity:")
        while not quantity.isdigit():
            quantity = input("Enter product quantity:")
        quantity = int(quantity)
        category=input("Enter product category : ")
        return cls(category,name,id,price,quantity)
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Price: {self.price} | Qty: {self.quantity} | Category: {self.category}"