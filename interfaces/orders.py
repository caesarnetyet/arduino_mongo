from dataclasses import dataclass, asdict

from interfaces.client import Client
from interfaces.product import Product


@dataclass
class Order:
    _id: str
    client: Client
    products: list[Product]
    total: float = 0.0

    def to_dict(self):
        return asdict(self)

    def get_total(self):
        total = 0
        for product in self.products:
            total += product.price
        self.total = total

    def __post_init__(self):
        self.get_total()
