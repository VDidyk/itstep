# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

string_list = []

while True:
    string = input("Enter a line or 'exit' in case you would like stop: ")
    if string == 'exit':
        break

    string_list.append(string)

filtered_list = [s for s in string_list if 'python' in s.lower()]
print(filtered_list)
