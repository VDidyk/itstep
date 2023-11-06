# До вже реалізованого класу «Країна» додайте конструктор та необхідні перевантажені методи

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

    def __lt__(self, other):
        return self._population < other.get_population()

    def __gt__(self, other):
        return self._population > other.get_population()

    def __eq__(self, other):
        return self._name == other._name and self._continent == other._continent

    def __str__(self):
        return (f"{self._name}, {self._continent} - Population: {self._population}, "
                f"Phone Code: {self._phone_code}, Capital: {self._capital}, "
                f"Cities: {', '.join(self._cities)}")

    def __repr__(self):
        return (f"Country(name='{self._name}', continent='{self._continent}', "
                f"population={self._population}, phone_code='{self._phone_code}', "
                f"capital='{self._capital}', cities={self._cities})")

    def show(self):
        print(self)


country = Country(
    name='Ukraine',
    continent='Europe',
    population=41000000,
    phone_code='+380',
    capital='Kyiv',
    cities=['Kyiv', 'Lviv', 'Odesa']
)

country1 = Country(
    name='Poland',
    continent='Europe',
    population=38000000,
    phone_code='+480',
    capital='Warsaw',
    cities=['Warsaw', 'Krakow', 'Lublin']
)

country.show()
country1.show()

print(country > country1)
