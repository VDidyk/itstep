# Створіть клас для конвертування з метричної системи в
# англійську, та навпаки. Реалізуйте функціональність у вигляді
# статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.

class MetricEnglishConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084

    @staticmethod
    def centimeters_to_inches(centimeters):
        return centimeters * 0.393701

    @staticmethod
    def inches_to_centimeters(inches):
        return inches / 0.393701


print(MetricEnglishConverter.meters_to_feet(20))
