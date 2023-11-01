# Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Person:
    _name: str = None
    _birth_date: str = None
    _phone: str = None
    _city: str = None
    _country: str = None
    _address: str = None

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


person = Person()

person.set_name('Vova')
person.set_birth_date('16.01.1994')
person.set_phone('+380637446378')
person.set_city('Lviv')
person.set_country('Ukraine')
person.set_address('Shevcnenka')

person.show()