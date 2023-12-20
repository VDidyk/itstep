# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран.
import random
import time
from threading import Thread

l = []


def fill():
    while True:
        l.append(random.randint(0, 100))
        time.sleep(2)


def s():
    while True:
        if len(l):
            print("SUM: " + str(sum(l)))
        time.sleep(2)


def avg():
    while True:
        if len(l):
            print("AVG:" + str(sum(l) / len(l)))
        time.sleep(2)


t1 = Thread(target=fill)
t2 = Thread(target=s)
t3 = Thread(target=avg)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
