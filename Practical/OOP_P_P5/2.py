# Створіть клас Passport (паспорт), який міститиме
# паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте
# клас ForeignPassport (закордонний паспорт), похідний
# від Passport.
# Нагадаємо, що закордонний паспорт містить, крім
# паспортних даних, дані про візи і номер закордонного
# паспорта.
# Кожен із класів має містити необхідні методи.

class Passport:
    def __init__(self, name, surname, number, country):
        self.country = country
        self.number = number
        self.surname = surname
        self.name = name

    def show(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Number: {self.number}")
        print(f"Country: {self.country}")


class ForeignPassport(Passport):
    def __init__(self, name, surname, number, country, is_biometric):
        super().__init__(name, surname, number, country)
        self.is_biometric = is_biometric

    def show(self):
        super().show()

        if self.is_biometric:
            print("Is biometric")
        else:
            print("Is not biometric")


passport = Passport('Vitalii', 'Didyk', 'KC546655', 'Ukraine')
passport.show()

f_passport = ForeignPassport('Vitalii', 'Didyk', 'KC546655', 'Ukraine', True)
f_passport.show()
