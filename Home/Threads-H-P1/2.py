# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
# кожен потік має записати у новий файл. Виведіть на екран
# статистику виконаних операцій.
import random
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


def fill(file):
    write(file, str([random.randint(0, 100) for _ in range(0, 100)]).replace('[', '').replace(']', ''))
    print('File has been filled')


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes(path):
    while True:
        data = read(path)

        if data:
            l = []
            for i in data.split(','):
                if is_prime(int(i)):
                    l.append(i)

            write('primes', str(l))
            print(f"{str(len(l))} primes have been written to file")
            break


def fact(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def find_fact(path):
    while True:
        data = read(path)

        if data:
            l = []
            for i in data.split(','):
                l.append(fact(int(i)))

            write('facts', str(l))
            print(f"{str(len(l))} facts have been written to file")
            break


file_path = input("Enter the file path: ")

t1 = Thread(target=lambda: fill(file_path))
t2 = Thread(target=lambda: find_primes(file_path))
t3 = Thread(target=lambda: find_fact(file_path))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
