# Створіть клас "Електронний Гаманець" додавши
# можливість видаляти та додавати гроші, а також перевіряти
# баланс

from datetime import datetime


class EWallet:
    __balance: float = None
    __history: list = []

    def __init__(self, balance: float = 0):
        self.__balance = 0

        self.__add_history(balance)

    def __add_history(self, amount):
        self.__history.append({
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount
        })

    def add_amount(self, amount: float):
        self.__balance += amount
        self.__add_history(amount)

    def sub_amount(self, amount: float):
        if amount < 0 or amount > self.__balance:
            raise ValueError("Wrong value")

        self.__balance -= amount
        self.__add_history(amount * -1)

    def show_balance(self):
        print(f"Balance is: {self.__balance}")

    def show_history(self):
        for x in self.__history:
            if x['amount'] < 0:
                color = '\033[31m'
            elif x['amount'] > 0:
                color = '\033[32m'
            else:
                color = '\033[37m'

            print(f"{color}{x['datetime']} - {x['amount']}\033[37m")


wallet = EWallet(1000)

wallet.add_amount(5000)
wallet.sub_amount(3000)
wallet.show_balance()
wallet.show_history()
