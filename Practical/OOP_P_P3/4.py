# Створіть клас "Комп'ютер", який має зберігати
# інформацію про процесор, ОЗУ та відеокарту. Застосуйте
# інкапсуляцію для захисту цих даних від змін.

class Computer:
    def __init__(self, cpu: str, ram: str, gpu: str):
        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu

    def get_cpu(self) -> str:
        return self.__cpu

    def get_ram(self) -> str:
        return self.__ram

    def get_gpu(self) -> str:
        return self.__gpu

    def set_cpu(self, cpu: str):
        self.__cpu = cpu

    def set_ram(self, ram: str):
        self.__ram = ram

    def set_gpu(self, gpu: str):
        self.__gpu = gpu


computer = Computer("Intel i9", "36GB", "NVIDIA GTX 1080Ti")
print(computer.get_cpu())
print(computer.get_ram())
print(computer.get_gpu())
