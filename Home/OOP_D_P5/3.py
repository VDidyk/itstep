# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання
# значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.


class Money:
    def __init__(self, usd, cents):
        self.usd = usd
        self.cents = cents

    def set_values(self, usd, cents):
        self.usd = usd
        self.cents = cents

    def display_money(self):
        print(f"{self.usd}.{self.cents:02d}")


class Product(Money):
    def __init__(self, name, usd, cents):
        super().__init__(usd, cents)
        self.name = name

    def set_discount(self, decrease_usd, decrease_cents):
        total_cents = self.usd * 100 + self.cents - (decrease_usd * 100 + decrease_cents)
        self.usd, self.cents = divmod(total_cents, 100)


money = Money(5, 50)
money.display_money()
money.set_values(8, 75)
money.display_money()

product = Product("Bread", 1, 50)
product.display_money()
product.set_discount(0, 25)
product.display_money()
