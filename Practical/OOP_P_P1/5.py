# Створіть клас BankAccount з атрибутами balance
# та owner, а також методами deposit та withdraw для
# здійснення операцій з балансом. Реалізуйте перевірку
# на те, що баланс не може стати від'ємним

class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError('The amount is more than the balance')

        self.balance -= amount

    def show_balance(self):
        print(f"Hello, {self.owner}! Your balance is {self.balance}")


account = BankAccount(1000, "Vitalii")

account.withdraw(500)
account.deposit(1000)

account.show_balance()
