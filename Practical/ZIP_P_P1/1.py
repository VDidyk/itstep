# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.

import zlib
import pickle

user_input_list = input("Enter numbers separating by coma: ").split(',')

compressed_data = zlib.compress(pickle.dumps(user_input_list))

file_path = 'compressed_data'
with open(file_path, 'wb') as file:
    file.write(compressed_data)

with open(file_path, 'rb') as file:
    read_compressed_data = file.read()
    decompressed_data = pickle.loads(zlib.decompress(read_compressed_data))

print(decompressed_data)