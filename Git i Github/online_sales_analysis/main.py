from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Phone", 800, 10))

print("Products:")
manager.display_products()
print("Total Inventory Value:", manager.total_inventory_value())