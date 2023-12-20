# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран


from threading import Thread

l = [int(x) for x in input("Enter numbers separating by coma: ").split(',')]

t1 = Thread(target=lambda: print("SUM: " + str(sum(l))))
t2 = Thread(target=lambda: print("AVG: " + str(sum(l) / len(l))))
t1.start()
t2.start()
t1.join()
t2.join()
