# Реалізуйте клас «Вебсайт». Збережіть у класі: назву
# вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
# та методи класу для введення-виведення даних, а також
# для інших операцій. Використовуйте механізм перевантаження методів.


class Website:
    def __init__(self, name=None, url=None, description=None):
        self.name = name
        self.url = url
        self.description = description

    def input(self):
        self.name = input("Enter website name: ")
        self.url = input("Enter website url: ")
        self.description = input("Website description: ")

    def show(self):
        print(self)

    def __str__(self):
        return f"Website '{self.name}': {self.url} - {self.description}"


website = Website("OpenAI", "https://openai.com",
                  "Організація, яка займається дослідженнями у сфері штучного інтелекту.")
website.show()

new_website = Website()
new_website.input()
new_website.show()

print(website)
