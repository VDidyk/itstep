# Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику

import sys

sys.path.append('../../../Libraries')
from Menu import Menu


def add_word(dictionary):
    word = input("Enter the word: ")
    definition = input("Enter the definition: ")
    dictionary[word] = definition


def delete_word(dictionary):
    word = input("Enter the word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print(f"Word '{word}' deleted from the dictionary.")
    else:
        print(f"Word '{word}' not found in the dictionary.")


def search_word(dictionary):
    word = input("Enter the word to search for: ")
    if word in dictionary:
        print(f"Definition of '{word}': {dictionary[word]}")
    else:
        print(f"Word '{word}' not found in the dictionary.")


dictionary = {}

menu = Menu()

menu.append("Add a word", lambda: add_word(dictionary))
menu.append("Delete a word", lambda: delete_word(dictionary))
menu.append("Search for a word", lambda: search_word(dictionary))

menu.start()
