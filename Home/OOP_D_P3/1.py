# Створіть систему управління замовленнями
# готелю. Кожне замовлення має містити інформацію
# про клієнта, тип кімнати, кількість днів проживання та
# вартість. Реалізуйте методи для додавання замовлення,
# зміни типу кімнати та кількості днів, а також
# видалення замовлення. Використайте інкапсуляцію для
# захисту вартості від неправильних змін.

from Order import OrdersContainer
from Order import Order


class HotelOrder(Order):
    _room_type: str = None
    _days: int = 0

    def __str__(self):
        return f"#{self.get_reference()} {self.get_client_name()} {self.get_room_type()} room {self.get_days()} days {self.get_total()} USD"

    def set_room_type(self, room_type: str):
        self._room_type = room_type

    def get_room_type(self) -> str:
        return self._room_type

    def set_days(self, days: int):
        self._days = days

    def get_days(self) -> int:
        return self._days


class HotelOrdersContainer(OrdersContainer):
    pass


orders_container = HotelOrdersContainer()

order = HotelOrder()
order.set_total(1000)
order.set_client_name("Vitalii Didyk")
order.set_days(5)
order.set_room_type('HB')

print(order)

orders_container.add(order)
order = orders_container.get_order_by_index(0)
order.set_room_type('BB')
order.set_days('7')

orders_container.show_orders()

orders_container.remove_order(order)
orders_container.show_orders()
