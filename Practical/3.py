# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

from threading import Thread


def write(path, data):
    with open(path, 'w') as file:
        file.write(data)


def read(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error")


def write_even(l):
    new_l = [x for x in l if int(x) % 2 == 0]
    write('even.txt', str(new_l))


def write_not_even(l):
    new_l = [x for x in l if int(x) % 2 != 0]
    write('not-even.txt', str(new_l))


file_path = input("Enter the file path: ")

l = read(file_path).split(' ')

t1 = Thread(target=lambda: write_even(l))
t2 = Thread(target=lambda: write_not_even(l))
t1.start()
t2.start()
t1.join()
t2.join()
