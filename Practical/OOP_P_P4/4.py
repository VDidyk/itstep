# Створіть клас InformationSystem, який має атрибут data
# - словник, де ключі - це імена користувачів, а значення -
# список їх контактів. Реалізуйте методи класу для додавання
# нових користувачів та їх контактів

class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user(self, user_name):
        if user_name not in self.data:
            self.data[user_name] = []

    def add_contact(self, user_name, contact):
        if user_name in self.data:
            self.data[user_name].append(contact)
        else:
            self.data[user_name] = [contact]

    def __str__(self):
        return f"{self.data}"


information = InformationSystem()
information.add_user('Tailer')
information.add_contact('Tailer', 'tailer12012@gmail.com')
information.add_contact('Tailer', 'tailer12015@gmail.com')

print(information)