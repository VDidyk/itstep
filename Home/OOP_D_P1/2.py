# Створіть клас «Місто». Збережіть у класі: назву міста,
# назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста, телефонний код міста. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій

class City:
    def __init__(self, name=None, region=None, country=None, population=None, postal_code=None, phone_code=None):
        self._name = name
        self._region = region
        self._country = country
        self._population = population
        self._postal_code = postal_code
        self._phone_code = phone_code

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_region(self, region: str):
        self._region = region

    def get_region(self) -> str:
        return self._region

    def set_country(self, country: str):
        self._country = country

    def get_country(self) -> str:
        return self._country

    def set_population(self, population: int):
        self._population = population

    def get_population(self) -> int:
        return self._population

    def set_postal_code(self, postal_code: str):
        self._postal_code = postal_code

    def get_postal_code(self) -> str:
        return self._postal_code

    def set_phone_code(self, phone_code: str):
        self._phone_code = phone_code

    def get_phone_code(self) -> str:
        return self._phone_code

    def show(self):
        print(f"City Name: {self._name}")
        print(f"Region: {self._region}")
        print(f"Country: {self._country}")
        print(f"Population: {self._population}")
        print(f"Postal Code: {self._postal_code}")
        print(f"Phone Code: {self._phone_code}")


city = City()

city.set_name('Lviv')
city.set_region('Lviv Oblast')
city.set_country('Ukraine')
city.set_population(720000)
city.set_postal_code('79000')
city.set_phone_code('+380 32')

city.show()
