class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def create_product(products, name, price):
    new_product = Product(name, price)
    products.append(new_product)
    print(f"Product '{name}' created successfully.")

def read_products(products):
    print("\nProducts:")
    for index, product in enumerate(products, 1):
        print(f"{index}. {product.name} - ${product.price:.2f}")

def update_product(products, index, name, price):
    if 0 < index <= len(products):
        product = products[index - 1]
        product.name = name
        product.price = price
        print(f"Product updated successfully.")
    else:
        print("Invalid index. Update failed.")

def delete_product(products, index):
    if 0 < index <= len(products):
        deleted_product = products.pop(index - 1)
        print(f"Product '{deleted_product.name}' deleted successfully.")
    else:
        print("Invalid index. Deletion failed.")

def sort_products_by_price(products):
    sorted_products = sorted(products, key=lambda x: x.price)
    return sorted_products

# Example usage
products = []

create_product(products, "Laptop", 1200.50)
create_product(products, "Smartphone", 599.99)
create_product(products, "Tablet", 349.99)

read_products(products)

sorted_products = sort_products_by_price(products)
print("\nSorted Products by Price:")
read_products(sorted_products)
