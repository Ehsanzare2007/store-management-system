from models.product import Product
from managers.storage_manager import StorageManager
class Manager:
    def __init__(self):
        self.products = []
        self.storage = StorageManager()
        self.products = self.storage.load_products()
    def add_product(self):
        product1=Product.add_product()
        for product in self.products:
            if product.id == product1.id:
                print("Product ID already exists.")
                return
        self.products.append(product1)
        self.storage.save_products(self.products)
    def show_product(self):
        for i in self.products:
            print(i)
    def search_product(self):
        while True:
            try:
                search_model=int(input('Do you want to search by ID or NAME? \n 1.Name \n 2.ID\nchoice:'))
                while search_model!=1 and search_model!=2:
                    search_model=int(input('Enter 1 or 2 : \n 1.Name \n 2.ID\nchoice:'))

                if search_model==1:
                    name_=input('Please enter product\'s name: ')
                    for product in self.products:
                        if product.name.lower()==name_.lower():
                            print(product)
                            return
                    print(f'{name_} not found')
                elif search_model==2:
                    ID_=input('Please enter product\'s ID: ')
                    for product in self.products:
                        if product.id==int(ID_):
                            print(product)
                            return
                    print('Product not found')
                break
            except ValueError:
                print('please enter 1 or 2 : ')
    def sell(self):
        try:
            p_id=int(input('Enter poduct\'s ID : '))
            sell_quantity=int(input('Enter many of sell :'))
            if sell_quantity <= 0:
                print("Quantity must be greater than 0.")
                return
            for product in self.products:
                if product.id == p_id:
                    if product.quantity >= sell_quantity:
                        product.quantity -= sell_quantity
                        self.storage.save_products(self.products)
                        print("Sale successful!")
                        print(f"Remaining quantity: {product.quantity}")
                    else:
                        print("Not enough stock!")

                    return

            print("Product not found.")

        except ValueError:
            print("Please enter valid numbers.")
    def edit_product(self):
        try:
            product_id = int(input("Enter product ID: "))

            for product in self.products:
                if product.id == product_id:

                    print(f"\nCurrent product:")
                    print(product)

                    while True:
                        choice = input(
                            "\n1. Edit Name\n"
                            "2. Edit Price\n"
                            "3. Edit Quantity\n"
                            "4. Edit Category\n"
                            "5. Back\n"
                            "Choose: "
                        )
                        if choice == "1":
                            new_name = input("Enter new name: ").strip()
                            if new_name:
                                product.name = new_name
                                print("Name updated successfully.")
                            else:
                                print("Name cannot be empty.")
                                continue
                        elif choice == "2":
                            while True:
                                try:
                                    new_price = float(input("Enter new price: "))
                                    if new_price < 0:
                                        print("Price cannot be negative.")
                                        continue
                                    product.price = new_price
                                    print("Price updated successfully.")
                                    break
                                except ValueError:
                                    print("Please enter a valid number.")
                        elif choice == "3":
                            while True:
                                try:
                                    new_quantity = int(input("Enter new quantity: "))
                                    if new_quantity < 0:
                                        print("Quantity cannot be negative.")
                                        continue
                                    product.quantity = new_quantity
                                    print("Quantity updated successfully.")
                                    break
                                except ValueError:
                                    print("Please enter a valid integer.")
                        elif choice == "4":
                            new_category = input(
                                "Enter new category: "
                            ).strip()
                            if new_category:
                                product.category = new_category
                                print("Category updated successfully.")
                            else:
                                print("Category cannot be empty.")
                                continue
                        elif choice == "5":
                            return
                        else:
                            print("Please choose between 1 and 5.")
                            continue
                        self.storage.save_products(self.products)
                        print("\nUpdated product:")
                        print(product)

                    return

            print("Product not found.")

        except ValueError:
            print("Please enter a valid product ID.")
    def delete_product(self):
        delete=input('Enter 1 or 2 ( for search product ) : \n1.Name\n2.ID\nfor delete product:')
        while not delete.isdigit() or delete not in ['1','2'] :
            delete=input('Enter 1 or 2 : \n1.Name\n2.ID\nfor search product:')
        if delete=='1':
            name=input('Enter pruduct\'s name : ')
            for p in self.products:
                if p.name==name:
                    d=input(f'Product details:\n{p}\nDo you want to delete? \n(Y/N):').upper()
                    while d not in 'YN':
                        d=input(f'Product details:\n{p}\nDo you want to delete? \n(Y/N):').upper()
                    if d=='Y':
                        print(f'{p.name} has been deleted')
                        self.products.remove(p)
                        self.storage.save_products(self.products)
                        return
                    else:
                        print(f'{p.name} has not deleted')
                        return
            print(f'{name} not found')
        if delete=='2':
                try:
                    id=int(input('Please enter product\'s ID : '))
                    for p in self.products:
                        if p.id==id:
                            d=input(f'Product details:\n{p}\nDo you want to delete? \n(Y/N):').upper()
                            while d not in 'YN':
                                d=input(f'Product details:\n{p}\nDo you want to delete? \n(Y/N):').upper()
                            if d=='Y':
                                print(f'{p.name} has been deleted')
                                self.products.remove(p)
                                self.storage.save_products(self.products)
                                return
                            else:
                                print(f'{p.name} has not deleted')
                                return
                    print(f'{p.name} not found')
                except ValueError:
                    print('Please enter nmuber (ID)')
    def inventory_value(self):
        value=0
        for p in self.products:
            v=p.quantity*p.price
            value+=v
        return value