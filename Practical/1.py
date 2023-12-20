# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

from threading import Thread

l = [int(x) for x in input("Enter numbers separating by coma: ").split(',')]

t1 = Thread(target=lambda: print("MAX: " + str(max(l))))
t2 = Thread(target=lambda: print("MIN: " + str(min(l))))
t1.start()
t2.start()
t1.join()
t2.join()
