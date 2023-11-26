# Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів

class TextModifier:
    def __init__(self, text):
        self.text: str = text

    def upper(self):
        return self.text.upper()

    def lower(self):
        return self.text.lower()

    def without_spaces(self):
        return self.text.replace(' ', '')

    def encypt_func(self, s=1):
        txt = self.text
        result = ""

        # transverse the plain txt
        for i in range(len(txt)):
            char = txt[i]
            # encypt_func uppercase characters in plain txt

            if (char.isupper()):
                result += chr((ord(char) + s - 64) % 26 + 65)
                # encypt_func lowercase characters in plain txt
            else:
                result += chr((ord(char) + s - 96) % 26 + 97)
        return result

    def __call__(self, *args, **kwargs):
        if args[0] == 'upper':
            return self.upper()
        elif args[0] == 'lower':
            return self.lower()
        elif args[0] == 'without-spaces':
            return self.without_spaces()
        elif args[0] == 'encypt':
            return self.encypt_func()


m = TextModifier("Hello world!")
print(m('upper'))
print(m('lower'))
print(m('without-spaces'))
print(m('encypt'))
