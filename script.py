import json
import sys

def read_orders(file_name):
    with open(file_name, 'r') as file:
        orders = json.load(file)
    return orders

def create_customers_json(orders):
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['name']
        customers[phone] = name

    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=2)

def main():
    if len(sys.argv) != 2:
        print("An file should be passed")
        sys.exit(1)

    orders_file = sys.argv[1]
    orders = read_orders(orders_file)
    
    create_customers_json(orders)

if __name__ == "__main__":
    main()
