# Python Store Management System

A simple command-line store management system built with Python.

This project was created to practice **Object-Oriented Programming (OOP)**, **JSON**, and **File Handling** in Python.

## Features

- Add products
- Show all products
- Search products by name or ID
- Sell products
- Edit product information
- Delete products
- Calculate total inventory value
- Save product data using JSON
- Load saved products when the program starts
- Basic input validation

## Technologies

- Python 3
- JSON
- Object-Oriented Programming
- File Handling

## Requirements

No external Python packages are required.

The project uses only Python's standard library.

Python 3.8 or newer is recommended.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/store-management-system.git
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

The program will display a menu:

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

## Project Structure

```text
store-management-system/
│
├── main.py
├── README.md
├── .gitignore
└── products.example.json
```

### main.py

Contains the main application and the following classes:

- `Product`
- `Manager`
- `StorageManager`
- `Menu`

### README.md

Contains documentation and instructions for using the project.

### .gitignore

Contains files that should not be uploaded to GitHub.

For example:

```text
products.json
__pycache__/
```

### products.example.json

Contains example product data and demonstrates the structure of the JSON file used by the application.

## Data Storage

The application stores product information in:

```text
products.json
```

This file is created and updated automatically by the program.

The actual `products.json` file is ignored by Git and is not uploaded to the repository.

## Example Product

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

The total inventory value is calculated using:

```text
Product Price × Product Quantity
```

For example:

```text
899.99 × 5 = 4499.95
```

## Future Improvements

Possible future features:

- Prevent duplicate product IDs
- Search products without case sensitivity
- Search by category
- Sort products
- Low-stock warnings
- Sales history
- Revenue tracking
- SQLite database
- Graphical User Interface (GUI)
- Automated tests

## License

This project is licensed under the MIT License.

## Author

Created as a Python learning project focused on Object-Oriented Programming, JSON, and File Handling.
