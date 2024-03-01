# Order Processing Script

This Python script is designed to process a file containing order information in JSON format. It reads the orders, extracts relevant information, and creates two separate JSON files: one for customer details (`customers.json`) and another for item details (`items.json`).

## File Structure

- **script.py**: The main Python script.

## Script Overview

### Dependencies
- The script uses the `json` and `sys` modules for handling JSON data and command-line arguments, respectively.

### Functions

#### `read_orders(file_name)`
- Reads the orders from the specified JSON file.
- Returns a Python dictionary containing order information.

#### `create_customers_json(orders)`
- Processes the orders to create a dictionary of customer phone numbers and names.
- Writes the customer information to a new JSON file (`customers.json`).

#### `create_items_json(orders)`
- Processes the orders to create a dictionary of item names, prices, and the number of orders for each item.
- Writes the item information to a new JSON file (`items.json`).

#### `main()`
- The main function that orchestrates the execution of the script.
- Verifies that a file name is provided as a command-line argument.
- Reads the orders from the specified file.
- Calls the functions to create customer and item JSON files.

### Usage

To run the script, provide the orders file as a command-line argument:

```bash
python script.py example_orders.json
