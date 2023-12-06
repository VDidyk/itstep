class Menu:
    def __init__(self):
        self.__items = []

    def append(self, name, callback):
        self.__items.append((name, callback))

    def start(self):
        for i, val in enumerate(self.__items):
            print(f"{i + 1}. {val[0]}")

            print(f"0. Exit")

        while True:
            choice = int(input("Make your choice: "))

            if choice == 0:
                break

            choice -= 1

            if 0 <= choice < len(self.__items):
                self.__items[choice][1]()
            else:
                print("Wrong option.")
