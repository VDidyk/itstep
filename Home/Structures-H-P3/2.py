# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно
import random
import time
from datetime import datetime

MAX_PASSENGERS = 30
MEAN_ARRIVAL_INTERVAL_PASSENGERS = 2
MEAN_ARRIVAL_INTERVAL_BOATS = 30
MIN_BOAT_CAPACITY = 2
MAX_BOAT_CAPACITY = 6
TIME_VALUE = 1


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def enqueue(self, item, ):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("Черга заповнена")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def show(self):
        if not self.is_empty():
            print("Елементи в черзі")
            for item in self.queue:
                print(f"Елемент {item}")
        else:
            print("Черга порожня")


class Dock:
    def __init__(self, env):
        self.env = env
        self.passengers = Queue(MAX_PASSENGERS)
        self.boats = Queue(50)
        self.current_time = 0
        self.waiting_time = []

    def passenger_arrival(self):
        if self.current_time % MEAN_ARRIVAL_INTERVAL_PASSENGERS == 0:
            p = Passenger()
            p.come()
            self.passengers.enqueue(p)

    def boat_arrival(self):
        if self.current_time % MEAN_ARRIVAL_INTERVAL_BOATS == 0:
            b = Boat(self.env, random.randint(MIN_BOAT_CAPACITY, MAX_BOAT_CAPACITY))
            b.come()
            self.boats.enqueue(b)

    def boarding(self):
        boat = self.boats.peek()

        if boat:
            for i in range(boat.free()):
                if not self.passengers.is_empty():
                    p = self.passengers.dequeue()
                    boat.board(p)
                    self.waiting_time.append((datetime.now() - p.arrival_time).total_seconds())

            if boat.free() == 0:
                boat = self.boats.dequeue()
                boat.go()

                print(f"{self.passengers.count()} are still in the queue")

    def wish_boat_interval(self):
        total_boats_needed = MAX_PASSENGERS / MIN_BOAT_CAPACITY
        total_time_for_passengers = MEAN_ARRIVAL_INTERVAL_PASSENGERS * MAX_PASSENGERS
        return total_time_for_passengers / total_boats_needed

    def statistics(self):
        print(f"Passengers are waiting: {self.passengers.count()}")
        print(f"Average of passenger waiting: {sum(self.waiting_time) / len(self.waiting_time)} s")
        print(f"Boat wish interval: {self.wish_boat_interval()}")

    def simulate(self):
        while True:
            self.passenger_arrival()
            self.boat_arrival()

            self.boarding()

            time.sleep(TIME_VALUE)
            self.current_time += TIME_VALUE

            if self.current_time % 10 == 0:
                self.statistics()


class Passenger:
    def __init__(self):
        self.arrival_time = datetime.now()

    def come(self):
        print(f"The passenger has come in {self.arrival_time}")


class Boat:
    def __init__(self, dock_type, capacity):
        self.dock_type = dock_type
        self.capacity = capacity
        self.passengers = []
        self.number = random.randint(1000, 10000)

    def free(self):
        return self.capacity - len(self.passengers)

    def board(self, passenger):
        self.passengers.append(passenger)
        print(f"The boat {self.number}. Passenger has been boarded. Loading is {len(self.passengers)}/{self.capacity}")

    def come(self):
        print(f"The boat with number {self.number} has come")

    def go(self):
        print(f"The boat with number {self.number} has sailed")


dock = Dock('')
dock.simulate()
