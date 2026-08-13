from managers.manager import Manager
class Menu:
    def __init__(self):
        self.manager = Manager()

    def run(self):
        while True:
            print("\n========== STORE MANAGER ==========")
            print("1. Add Product")
            print("2. Show Products")
            print("3. Search Product")
            print("4. Sell Product")
            print("5. Edit Product")
            print("6. Delete Product")
            print("7. Inventory Value")
            print("8. Exit")
            print("===================================")

            choice = input("Choose an option: ")

            if choice == "1":
                self.manager.add_product()

            elif choice == "2":
                self.manager.show_product()

            elif choice == "3":
                self.manager.search_product()

            elif choice == "4":
                self.manager.sell()

            elif choice == "5":
                self.manager.edit_product()

            elif choice == "6":
                self.manager.delete_product()

            elif choice == "7":
                value = self.manager.inventory_value()
                print(f"Total inventory value: {value:.2f}")

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
start=Menu()
start.run()