# Реалізуйте клас "Кошик для покупок" з можливістю
# додавання товарів та підрахунку загальної вартості.
# Застосуйте інкапсуляцію для забезпечення правильності
# обробки даних.

from dataclasses import dataclass
import random


def create_random_product():
    product = Product()
    product.set_id(random.randint(1, 1000))
    product.set_name(realistic_product_name())
    product.set_price(round(random.uniform(1.0, 1000.0), 2))
    return product


def realistic_product_name():
    products = [
        "Desk Lamp", "Wall Clock", "Coffee Mug", "Bluetooth Speaker",
        "Smartphone Case", "Notebook", "Sunglasses", "Backpack",
        "Water Bottle", "Wireless Charger", "Earbuds", "Wristwatch",
        "Tablet Stand", "Mouse Pad", "Document Holder", "Hand Sanitizer",
        "USB Flash Drive", "Pen Holder", "Calendar", "Keychain"
    ]
    return random.choice(products)


@dataclass
class Product:
    __id: int = None
    __name: str = None
    __price: float = None

    def set_id(self, product_id: int):
        self.__id = product_id

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_price(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price


class ProductsContainer:
    __products: dict = None

    def __init__(self):
        self.__products = {}

    def __str__(self):
        monitor = ''

        key = 1
        for item in self.__products.values():
            monitor += f"{key}. {item['product'].get_name()} ({item['product'].get_price()}) USD - {item['qty']} qty\n"
            key += 1

        return monitor

    def add_product(self, product: Product, qty: int):
        if product.get_id() not in self.__products:
            self.__products[product.get_id()] = {
                'product': product,
                'qty': 0
            }

        self.__products[product.get_id()]['qty'] += qty

    def get_total(self):
        return str(round(sum(map(lambda x: x['qty'] * x['product'].get_price(), self.__products.values())), 2)) + ' USD'


realistic_products_array = []
for _ in range(20):
    product = create_random_product()
    product.set_name(realistic_product_name())
    realistic_products_array.append(product)

container = ProductsContainer()
for product in realistic_products_array:
    container.add_product(product, random.randint(1, 10))

print(container.get_total())
