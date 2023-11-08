import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


class Order:
    _total: float = 0
    _client_name: str = None
    _reference: str = random.random()

    def __init__(self):
        self._reference = generate_random_string(7)

    def get_reference(self) -> str:
        return self._reference

    def get_total(self) -> float:
        return self._total

    def set_total(self, total: float):
        self._total = total

    def set_client_name(self, name: str):
        self._client_name = name

    def get_client_name(self) -> str:
        return self._client_name


class OrdersContainer:
    _orders: list = []

    def add(self, order: Order):
        self._orders.append(order)

    def get_order_by_index(self, index: int) -> Order:
        return self._orders[index]

    def remove_order(self, order: Order):
        self._orders.remove(order)

    def show_orders(self):
        if len(self._orders):
            [print(order) for order in self._orders]
        else:
            print("There is no orders")
