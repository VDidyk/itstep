# Створіть клас Car з атрибутами brand (марка
# автомобіля), model (модель) та year (рік випуску).
# Додайте метод start_engine, який виведе повідомлення
# про те, що двигун запущено.

from TaskFour.Cars.BMW import BMW
from TaskFour.Cars.Ferrari import Ferrari

cars = [
    BMW(),
    Ferrari()
]

for car in cars:
    car.start_engine()
