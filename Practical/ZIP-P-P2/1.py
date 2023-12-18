# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану за
# допомогою завантаження даних з JSON-файлу.

import json
import random
import time
from datetime import datetime, timedelta


def save_state(state, filename='timer_state.json'):
    with open(filename, 'w') as file:
        json.dump(state, file)


def load_state(filename='timer_state.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def start_timer():
    state = load_state()
    start_time = state.get('start_time') if state else datetime.now().timestamp()

    try:
        while True:
            20 / random.randint(0, 10)
            current_time = datetime.now().timestamp()
            elapsed_time = timedelta(seconds=int(current_time - start_time))
            print(f"Elapsed Time: {elapsed_time}", end='\r', flush=True)
            time.sleep(1)
    except ZeroDivisionError:
        save_state({'start_time': start_time})
        print("\nTimer stopped and state saved.")


start_timer()
