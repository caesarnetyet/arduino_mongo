import uuid
from dataclasses import asdict
from database.parse_json import ParseJson
from controllers.orders_controller import OrdersController
from interfaces.client import Client
from interfaces.orders import Order
from interfaces.product import Product

orders_controller = OrdersController()


client = Client(1, "John", "123456789")
product = Product(1, "Product 1", 10.0)
product2 = Product(2, "Product 2", 20.0)
product3 = Product(3, "Product 3", 30.0)
order = Order(uuid.uuid4().__str__(), client, [product, product2, product3])

orders_controller.add_order(order)

