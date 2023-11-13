# Створіть клас FileUtils, який має метод класу
# count_lines, який приймає шлях до файлу і повертає
# кількість рядків у файлі.

class FileUtils:
    @staticmethod
    def count_lines(file_path):
        try:
            with open(file_path, 'r') as file:
                return sum(1 for _ in file)
        except FileNotFoundError:
            return "File was not found"
        except Exception as e:
            return f"Error"


print(FileUtils.count_lines('test.txt'))
