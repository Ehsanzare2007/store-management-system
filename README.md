# Python Store Management System

A simple command-line store management system built with Python.

This project was created to practice Object-Oriented Programming (OOP), JSON data storage, file handling, input validation, and modular Python project structure.

## Features

* Add new products
* Display all products
* Search products by name or ID
* Sell products and update stock
* Edit product information
* Delete products
* Calculate total inventory value
* Save product data using JSON
* Load saved products automatically when the program starts
* Basic input validation
* Confirmation before deleting products

## Technologies

* Python 3
* JSON
* Object-Oriented Programming
* File Handling

## Requirements

No external Python packages are required.

The project uses only Python's standard library.

Python 3.8 or newer is recommended.

## Installation

Clone the repository:

```bash
git clone https://github.com/Ehsanzare2007/store-management-system.git
```

Move into the project directory:

```bash
cd store-management-system
```

## Running the Program

Run the following command:

```bash
python main.py
```

The program will display the main menu:

```text
========== STORE MANAGER ==========
1. Add Product
2. Show Products
3. Search Product
4. Sell Product
5. Edit Product
6. Delete Product
7. Inventory Value
8. Exit
===================================
```

Select an option by entering its corresponding number.

## Project Structure

```text
store-management-system/
│
├── main.py
│
├── models/
│   └── product.py
│
├── managers/
│   ├── manager.py
│   └── storage_manager.py
│
├── ui/
│   └── menu.py
│
├── products.example.json
├── .gitignore
├── LICENSE
└── README.md
```

## File Description

### `main.py`

The entry point of the application.

It imports the `Menu` class and starts the program.

### `models/product.py`

Contains the `Product` class.

The class represents a product and stores:

* Product ID
* Product name
* Price
* Quantity
* Category

It also provides functionality for creating products and converting product objects into dictionary data for JSON storage.

### `managers/manager.py`

Contains the `Manager` class.

It handles the main store operations:

* Adding products
* Displaying products
* Searching for products
* Selling products
* Editing products
* Deleting products
* Calculating inventory value

### `managers/storage_manager.py`

Contains the `StorageManager` class.

It is responsible for storing and loading product information using JSON.

It converts product objects into JSON-compatible data when saving and recreates `Product` objects when loading data.

### `ui/menu.py`

Contains the `Menu` class.

It provides the command-line interface and connects user selections to the appropriate manager operations.

### `products.example.json`

Contains example product data and demonstrates the structure used by the application for JSON storage.

The actual `products.json` file is generated locally when the program runs and is excluded from Git using `.gitignore`.

## Data Storage

The application uses JSON for persistent product storage.

Product information is stored locally in:

```text
products.json
```

This file is automatically created and updated when products are added, edited, sold, or deleted.

When the application starts, previously saved products are loaded from the JSON file.

The `products.json` file is excluded from the repository because it contains local application data.

## Example Product

A product is stored in JSON format similar to:

```json
{
    "category": "Electronics",
    "name": "Laptop",
    "id": 101,
    "price": 899.99,
    "quantity": 5
}
```

## Inventory Value

The total inventory value is calculated by multiplying the price of each product by its available quantity.

```text
Product Price × Product Quantity
```

For example:

```text
899.99 × 5 = 4499.95
```

The total value of all products is displayed through the `Inventory Value` option.

## Future Improvements

Possible future improvements include:

* Prevent duplicate product IDs
* Make product searches case-insensitive
* Search products by category
* Add product sorting and filtering
* Add low-stock warnings
* Add sales history
* Add revenue tracking
* Improve input validation
* Add automated tests
* Add SQLite database support
* Add a graphical user interface

## Learning Goals

This project was created to practice:

* Python classes and objects
* Object-Oriented Programming
* Class methods
* Modular project organization
* File handling
* JSON serialization and deserialization
* Input validation
* Exception handling
* Basic inventory management
* Git and GitHub workflow

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

## Author

Ehsan Zare

GitHub: https://github.com/Ehsanzare2007
