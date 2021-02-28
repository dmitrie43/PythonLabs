from models.Product import Product
from models.Warehouse import Warehouse

product = Product()
# product.add_new_product(product_name='SkyLine3', price=8790, article='22LT5906')
products = product.get_all_products(with_quantity=True)
for elem in products:
    print(elem)

# warehouse = Warehouse()
# warehouse.update_product_quantity(2, 15)

