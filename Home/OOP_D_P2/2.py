# До вже реалізованого класу «Місто» додайте конструктор та необхідні перевантажені методи.

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

    def __str__(self):
        return (f"{self._name}, {self._region}, {self._country} - Population: {self._population}, "
                f"Postal Code: {self._postal_code}, Phone Code: {self._phone_code}")

    def __repr__(self):
        return (f"City(name='{self._name}', region='{self._region}', country='{self._country}', "
                f"population={self._population}, postal_code='{self._postal_code}', "
                f"phone_code='{self._phone_code}')")

    def __eq__(self, other):
        return self._population == other.get_population()

    def __lt__(self, other):
        return self._population < other.get_population()

    def __gt__(self, other):
        return self._population > other.get_population()

    def show(self):
        print(f"City Name: {self._name}")
        print(f"Region: {self._region}")
        print(f"Country: {self._country}")
        print(f"Population: {self._population}")
        print(f"Postal Code: {self._postal_code}")
        print(f"Phone Code: {self._phone_code}")


city = City(
    name='Kyiv',
    region='Kyiv',
    country='Ukraine',
    population=2962180,
    postal_code='02000',
    phone_code='+380'
)

city1 = City(
    name='Lviv',
    region='Lviv',
    country='Ukraine',
    population=750000,
    postal_code='045',
    phone_code='+380'
)

print(city)
print(repr(city))
print(city == city1)
