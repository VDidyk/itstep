# До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
# створених об’єктів класу «Людина».

class Person:
    _instances = 0

    def __init__(self, name=None, birth_date=None, phone=None, city=None, country=None, address=None):
        self._name = name
        self._birth_date = birth_date
        self._phone = phone
        self._city = city
        self._country = country
        self._address = address

        Person._instances += 1

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_birth_date(self, date: str):
        self._birth_date = date

    def get_birth_date(self) -> str:
        return self._birth_date

    def set_phone(self, phone: str):
        self._phone = phone

    def get_phone(self) -> str:
        return self._phone

    def set_city(self, city: str):
        self._city = city

    def get_city(self) -> str:
        return self._city

    def set_country(self, country: str):
        self._country = country

    def get_country(self) -> str:
        return self._country

    def set_address(self, address: str):
        self._address = address

    def get_address(self) -> str:
        return self._address

    def show(self):
        print(f"Name: {self._name}")
        print(f"Birth: {self._birth_date}")
        print(f"Phone: {self._phone}")
        print(f"City: {self._city}")
        print(f"Country: {self._country}")
        print(f"Address: {self._address}")

    def __str__(self):
        return (f"Name: {self._name}, "
                f"Birth Date: {self._birth_date}, "
                f"Phone: {self._phone}, "
                f"City: {self._city}, "
                f"Country: {self._country}, "
                f"Address: {self._address}")

    def __repr__(self):
        return (f"Person(name='{self._name}', "
                f"birth_date='{self._birth_date}', "
                f"phone='{self._phone}', "
                f"city='{self._city}', "
                f"country='{self._country}', "
                f"address='{self._address}')")

    def __eq__(self, other):
        return self._name == other.get_name()

    @staticmethod
    def get_instance_count():
        return Person._instances


person = Person()

person.set_name('Vova')
person.set_birth_date('16.01.1994')
person.set_phone('+380637446378')
person.set_city('Lviv')
person.set_country('Ukraine')
person.set_address('Shevcnenka')

person.show()
print(person)
print(repr(person))

print(Person.get_instance_count())