# Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

import random

l = [random.randint(0, 100) for x in range(0, random.randint(0, 100))]
l1 = list(filter(lambda x: x % 2 == 0, l))

print(l1)
