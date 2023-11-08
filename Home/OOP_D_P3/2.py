# Розробіть систему управління замовленнями таксі.
# Кожне замовлення має містити інформацію про
# клієнта, адресу, тип автомобіля та вартість. Реалізуйте
# методи для додавання нових замовлень, зміни адреси та
# типу автомобіля, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від
# неправильних змін.

from Order import OrdersContainer
from Order import Order


class TaxiOrder(Order):
    _address: str = None
    _car: str = None

    def __str__(self):
        return f"#{self.get_reference()} {self.get_client_name()} {self.get_car()} {self.get_address()} {self.get_total()} USD"

    def set_address(self, address: str):
        self._address = address

    def get_address(self) -> str:
        return self._address

    def set_car(self, car: str):
        self._car = car

    def get_car(self) -> str:
        return self._car


class TaxiOrdersContainer(OrdersContainer):
    pass


orders_container = TaxiOrdersContainer()

order = TaxiOrder()
order.set_total(20)
order.set_client_name("Vitalii Didyk")
order.set_address("Chornovola 23")
order.set_car('Mazda CX5')

print(order)

orders_container.add(order)
order = orders_container.get_order_by_index(0)
order.set_address('Chornovola 1')
order.set_car('Mazda CX6')

orders_container.show_orders()

orders_container.remove_order(order)
orders_container.show_orders()
