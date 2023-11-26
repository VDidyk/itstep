# Іноді ви можете використати property() для створення
# доступу до атрибутів через геттери та сеттери для
# забезпечення певних перевірок або операцій перед
# отриманням або зміною атрибутів. Створіть клас для
# роботи з банківським рахунком, щоб гроші знялися або
# зарахувалися тільки при виконанні певних умов
# (наприклад, якщо гроші на рахунку є).

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        if amount > self._balance:
            raise ValueError
        self._balance -= amount


account = BankAccount(10000)
account.deposit(500)
account.withdraw(200)
print(account.balance)
