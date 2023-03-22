from faker import Faker


class Locale:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            'name': self.fake.name()
        }

    def build(self):
        return self.result
