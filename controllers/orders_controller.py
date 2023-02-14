from database import Database
from interfaces.orders import Order


class OrdersController:
    def __init__(self):
        self.orders: list[Order] = []
        self.db = Database("test", "orders")

    def add_order(self, order: Order):
        self.orders.append(order)
        dict_order = order.to_dict()
        self.db.insert(dict_order)

    def get_orders(self):
        return self.orders
