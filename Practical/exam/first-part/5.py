# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

string_list = []

while True:
    string = input("Enter a line or 'exit' in case you would like stop: ")
    if string == 'exit':
        break

    string_list.append(string)

capitalized = [s for s in string_list if s[0].isupper()]
print(capitalized)
