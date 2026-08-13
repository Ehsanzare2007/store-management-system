# Store Management System

A simple command-line store management system built with Python. This project demonstrates object-oriented programming, JSON-based data storage, file handling, input validation, and basic inventory management.

The project was developed as a learning project to practice Python classes, object-oriented programming, file handling, and working with JSON data.

## Features

* Add new products
* Display all products
* Search products by name or ID
* Sell products and update inventory
* Edit product information
* Delete products
* Calculate total inventory value
* Save product data using JSON
* Load saved products automatically when the program starts
* Input validation for product price, quantity, and ID
* Confirmation before deleting products

## Technologies Used

* Python 3
* JSON
* Object-Oriented Programming
* File Handling

No external Python packages are required.

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

### File and Directory Description

#### `main.py`

The entry point of the application. It creates the menu and starts the program.

#### `models/product.py`

Contains the `Product` class.

The class represents a product and stores information such as:

* Product ID
* Product name
* Price
* Quantity
* Category

#### `managers/manager.py`

Contains the `Manager` class.

It handles the main product management operations:

* Adding products
* Showing products
* Searching
* Selling
* Editing
* Deleting
* Calculating inventory value

#### `managers/storage_manager.py`

Contains the `StorageManager` class.

It is responsible for:

* Saving products to JSON
* Loading products from JSON
* Converting JSON data back into `Product` objects

#### `ui/menu.py`

Contains the command-line interface of the application.

It displays the main menu and connects user choices to the appropriate manager functions.

#### `products.example.json`

An example of the JSON structure used to store product information.

The actual `products.json` file is generated locally by the application and is excluded from Git using `.gitignore`.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ehsanzare2007/store-management-system.git
```

### 2. Navigate to the project directory

```bash
cd store-management-system
```

### 3. Make sure Python is installed

Check your Python version:

```bash
python --version
```

Python 3.x is recommended.

No additional packages or dependencies are required.

## Usage

Run the application with:

```bash
python main.py
```

The program will display the following menu:

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

Choose an option by entering the corresponding number.

### Example

To add a product:

```text
Choose an option: 1

Enter product name: Laptop
Enter product id: 101
Enter product price: 850
Enter product quantity: 5
Enter product category: Electronics
```

The product will be added to the inventory and saved to the local JSON file.

To display the products:

```text
Choose an option: 2

ID: 101 | Name: Laptop | Price: 850.0 | Qty: 5 | Category: Electronics
```

## Data Storage

The application uses a JSON file to store product information.

When products are added, edited, sold, or deleted, the data is saved to:

```text
products.json
```

When the application starts, it automatically loads the previously saved products.

The `products.json` file is intentionally excluded from the Git repository because it contains local application data.

## Requirements

* Python 3.x
* No external libraries are required.

The `json` module is part of Python's standard library.

## Current Limitations

This project is currently a command-line application and is intended primarily for learning and practice.

Some possible improvements include:

* Preventing duplicate product IDs
* Improving search functionality
* Adding low-stock warnings
* Adding sales history
* Adding product sorting and filtering
* Adding automated tests
* Improving error handling
* Adding a graphical user interface
* Migrating from JSON storage to a database for larger datasets

## Future Improvements

Planned improvements may include:

1. Unique product ID validation
2. Low-stock notifications
3. Sales history and transaction records
4. Product sorting and filtering
5. Unit tests
6. Improved command-line interface
7. Database support
8. Graphical user interface

## Learning Goals

This project was created to practice and demonstrate:

* Python classes and objects
* Object-oriented programming
* Class methods
* Encapsulation of responsibilities
* File handling
* JSON serialization and deserialization
* Input validation
* Exception handling
* Modular project structure
* Basic Git and GitHub workflow

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

## Author

Ehsan Zare

GitHub:

https://github.com/Ehsanzare2007
