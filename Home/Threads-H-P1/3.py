# Користувач вводить з клавіатури шлях до існуючої та
# до нової директорії. Після чого запускається потік, який має
# скопіювати вміст директорії у нове місце. Збережіть структуру
# директорії. Виведіть статистику виконаних операцій на екран.

import os
import shutil
from threading import Thread


def copy_directory(src, dst):
    try:
        os.makedirs(dst, exist_ok=True)
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except Exception as e:
        print(f"Error: {e}")


src = input("Enter the path to the existing directory: ")
dst = input("Enter the path to the new directory: ")

if os.path.exists(src):
    copy_thread = Thread(target=copy_directory, args=(src, dst))
    copy_thread.start()
    copy_thread.join()

    num_files = sum(len(files) for _, _, files in os.walk(dst))
    print(f"Copied {num_files} files to {dst}")
