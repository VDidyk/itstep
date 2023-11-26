# Створіть дескриптор для атрибуту, що зберігає
# розмір файлу. Додайте можливість зберігати розмір
# файлу в байтах, але представляти його у зручному для
# читання форматі (наприклад, КБ або МБ).

class FileSizeDescriptor:
    size_bytes = 0

    def __get__(self, instance, owner):
        print(self)
        print(instance)
        print(owner)
        return self

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("розмір файлу не меньше 0")
        self.size_bytes = value

    def formatted(self):
        if self.size_bytes < 1024:
            return f'{self.size_bytes} Б'
        elif self.size_bytes < 1024 ** 2:
            return f'{self.size_bytes / 1024} КБ'
        elif self.size_bytes < 1024 ** 3:
            return f'{self.size_bytes / 1024 ** 2} MБ'
        else:
            return f'{self.size_bytes / 1024 ** 3} ГБ'


class File:
    size = FileSizeDescriptor()


file = File()
file.size = 10240000
print(file.size.formatted())
