# Створіть базовий клас Clock, який містить атрибути
# години та хвилини. Від цього базового класу
# успадковуйте два класи: AnalogClock та DigitalClock.
# Клас AnalogClock повинен мати метод display_time,
# який виводить поточний час у форматі
# "години:хвилини". Клас DigitalClock повинен мати
# метод display_time, який виводить поточний час у
# цифровому форматі "гг:хх".
# Створіть об'єкти кожного класу та виведіть
# поточний час за допомогою методу display_time.

class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


class AnalogClock(Clock):
    def display_time(self):
        return f"{self.hours}:{self.minutes}"


class DigitalClock(Clock):
    def display_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


analog_clock = AnalogClock(4, 15)
digital_clock = DigitalClock(4, 15)

print(analog_clock.display_time())
print(digital_clock.display_time())
