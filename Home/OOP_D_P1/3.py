# Створіть клас «Країна». Збережіть у класі: назву країни,
# назву континенту, кількість жителів країни, телефонний
# код країни, назву столиці, назву міст країни. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.

class Country:
    def __init__(self, name=None, continent=None, population=None, phone_code=None, capital=None, cities=None):
        self._name = name
        self._continent = continent
        self._population = population
        self._phone_code = phone_code
        self._capital = capital
        self._cities = cities or []

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_continent(self, continent: str):
        self._continent = continent

    def get_continent(self) -> str:
        return self._continent

    def set_population(self, population: int):
        self._population = population

    def get_population(self) -> int:
        return self._population

    def set_phone_code(self, phone_code: str):
        self._phone_code = phone_code

    def get_phone_code(self) -> str:
        return self._phone_code

    def set_capital(self, capital: str):
        self._capital = capital

    def get_capital(self) -> str:
        return self._capital

    def set_cities(self, cities: list):
        self._cities = cities

    def get_cities(self) -> list:
        return self._cities

    def add_city(self, city: str):
        self._cities.append(city)

    def show(self):
        print(f"Country Name: {self._name}")
        print(f"Continent: {self._continent}")
        print(f"Population: {self._population}")
        print(f"Phone Code: {self._phone_code}")
        print(f"Capital: {self._capital}")
        print(f"Cities: {', '.join(self._cities)}")


country = Country()

country.set_name('Ukraine')
country.set_continent('Europe')
country.set_population(41000000)
country.set_phone_code('+380')
country.set_capital('Kyiv')
country.set_cities(['Kyiv', 'Lviv', 'Odesa'])

country.show()
