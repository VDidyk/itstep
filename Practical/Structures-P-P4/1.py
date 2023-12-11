# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький
# або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти
# переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник
# звернень);
# ■ відображати топ-10 найнепопулярніших слів
# (визначаємо непопулярність спираючись на лічильник
# звернень).
# Використовуйте дерево для виконання цього
# завдання.

import sys

sys.path.append('../../Libraries')
from Menu import Menu


def word_to_int(word):
    result = 0
    for char in word:
        result = result * 31 + ord(char)
    return result


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, word, translation):
        self.count += 1

        value = {
            "id": word_to_int(word),
            "word": word,
            "translation": translation,
            "usage": 0
        }

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        if value["id"] < current_node.value["id"]:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)

        elif value["id"] > current_node.value["id"]:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)

    def update(self, word, new_word):
        value = self.search(word)
        if value:
            value["id"] = word_to_int(new_word)
            value["word"] = new_word
        else:
            print(f"Word '{word}' not found.")

    def update_translation(self, word, new_translation):
        value = self.search(word)
        if value:
            value["translation"] = new_translation
        else:
            print(f"Word '{word}' not found.")

    def delete(self, word):
        self.root = self._delete_recursive(self.root, word_to_int(word))

    def _delete_recursive(self, current_node, word_id):
        if current_node is None:
            return None

        if word_id < current_node.value["id"]:
            current_node.left = self._delete_recursive(current_node.left, word_id)
        elif word_id > current_node.value["id"]:
            current_node.right = self._delete_recursive(current_node.right, word_id)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            min_larger_node = self._get_min_node(current_node.right)
            current_node.value = min_larger_node.value
            current_node.right = self._delete_recursive(current_node.right, min_larger_node.value["id"])

        return current_node

    def search(self, value):
        value = word_to_int(value)
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, current_node):
        if current_node is None:
            return False
        elif current_node.value["id"] == value:
            current_node.value["usage"] += 1
            return current_node.value
        elif value < current_node.value["id"]:
            return self._search_recursive(value, current_node.left)
        else:
            return self._search_recursive(value, current_node.right)

    def inorder_travelsal(self):
        self._inorder_travelsal_recursive(self.root)

    def _inorder_travelsal_recursive(self, current_node):
        if current_node is not None:
            self._inorder_travelsal_recursive(current_node.left)
            print(current_node.value)
            self._inorder_travelsal_recursive(current_node.right)

    def collect_words(self):
        words = []
        self._collect_words_recursive(self.root, words)
        return words

    def _collect_words_recursive(self, current_node, words):
        if current_node is not None:
            self._collect_words_recursive(current_node.left, words)
            words.append(current_node.value)
            self._collect_words_recursive(current_node.right, words)

    def top_usage_words(self, top_n=10, least=False):
        words = self.collect_words()
        words.sort(key=lambda x: x['usage'], reverse=not least)
        return words[:top_n]


class Dictionary:
    def __init__(self):
        self.dictionary = BinaryTree()
        self.access_count = {}

    def show(self):
        print(self.dictionary.inorder_travelsal())

    def add_word(self, word, translation):
        self.dictionary.insert(word, translation)

    def find_word(self, word):
        value = self.dictionary.search(word)
        if value:
            print(f"{value['word']}:{value['translation']}")

    def update(self, word, new_word):
        self.dictionary.update(word, new_word)

    def update_translation(self, word, new_translation):
        self.dictionary.update_translation(word, new_translation)

    def delete(self, word):
        self.dictionary.delete(word)

    def show_top_words(self, top_n=10, least=False):
        top_words = self.dictionary.top_usage_words(top_n, least)
        for word in top_words:
            print(f"{word['word']}:{word['translation']} (Usage: {word['usage']})")


d = Dictionary()
d.add_word("Apple", "Яблуко")
d.add_word("Hello", "Привіт")
d.add_word("Book", "Книга")
d.add_word("Sun", "Сонце")
d.add_word("Moon", "Місяць")
d.add_word("Star", "Зірка")
d.add_word("Sky", "Небо")
d.add_word("River", "Річка")
d.add_word("Mountain", "Гора")
d.add_word("Tree", "Дерево")
d.add_word("Flower", "Квітка")
d.add_word("Bird", "Птах")
d.add_word("Cat", "Кіт")
d.add_word("Dog", "Собака")
d.add_word("Fish", "Риба")
d.add_word("Car", "Автомобіль")
d.add_word("Bicycle", "Велосипед")
d.add_word("Road", "Дорога")
d.add_word("City", "Місто")
d.add_word("Village", "Село")
d.add_word("House", "Будинок")
d.add_word("School", "Школа")
d.add_word("University", "Університет")
d.add_word("Chair", "Стілець")
d.add_word("Table", "Стіл")
d.add_word("Window", "Вікно")
d.add_word("Door", "Двері")
d.add_word("Computer", "Комп'ютер")
d.add_word("Phone", "Телефон")
d.add_word("Television", "Телевізор")


menu = Menu()

menu.append("Show dictionary", lambda: d.show())
menu.append("Add world", lambda: d.add_word(input("Write word: "), input("Write translation: ")))
menu.append("Find word", lambda: d.find_word(input("Write word: ")))
menu.append("Update word", lambda: d.update(input("Write word: "), input("Write new word: ")))
menu.append("Update translation", lambda: d.update_translation(input("Write word: "), input("Write new translation: ")))
menu.append("Delete word", lambda: d.delete(input("Write word: ")))
menu.append("Show top words", lambda: d.show_top_words())
menu.append("Show top 10 least popular words", lambda: d.show_top_words(least=True))
menu.start()
