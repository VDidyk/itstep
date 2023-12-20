# Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
# потоки. Перший потік має знайти файли з потрібним словом
# і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
# заборонених слів (список цих слів потрібно зчитати з файлу
# із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.

import os
import threading


def search_and_merge_files(directory, search_word, output_file):
    matched_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if search_word in f.read():
                        matched_files.append(file_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    try:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for file_path in matched_files:
                with open(file_path, 'r', encoding='utf-8') as f_in:
                    f_out.write(f_in.read() + "\n")
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

    print(f"Found {len(matched_files)} files containing the word '{search_word}'.")
    print(f"Merged content into {output_file}.")


def remove_forbidden_words(output_file, forbidden_words_file):
    search_thread.join()

    try:
        with open(forbidden_words_file, 'r', encoding='utf-8') as f:
            forbidden_words = f.read().splitlines()

        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        for word in forbidden_words:
            content = content.replace(word, '')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Removed forbidden words from {output_file}.")

    except Exception as e:
        print(f"Error processing file {output_file}: {e}")


directory = input("Enter the path to the existing directory: ")
search_word = input("Enter the word to search for: ")
output_file = "merged_content.txt"
forbidden_words_file = "forbidden_words.txt"

if not os.path.exists(directory):
    print("The specified directory does not exist.")
else:
    search_thread = threading.Thread(target=search_and_merge_files, args=(directory, search_word, output_file))
    search_thread.start()

    filter_thread = threading.Thread(target=remove_forbidden_words, args=(output_file, forbidden_words_file))
    filter_thread.start()
