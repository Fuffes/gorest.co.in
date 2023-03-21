from faker import Faker


class Locale:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            'name': self.fake.name()
        }

    def build(self):
        return self.result

w = Locale('en_US').build()
y = Locale('ru_RU').build()

print(w)
print(y)