# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

from threading import Thread


def read(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error")


def search(text, search_word):
    index = 0

    for w in text.split():
        if w == search_word:
            print("The searched index is: " + str(index))

        index += 1


file_path = input("Enter the file path: ")
search_word = input("Enter the search word: ")

text = read(file_path)

t1 = Thread(target=lambda: search(text, search_word))

t1.start()
t1.join()
