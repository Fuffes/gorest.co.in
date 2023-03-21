from src.enums.user_enums import Status
from src.generator.player_locale import Locale


class Player():

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Status.ACTIVE.value):
        self.result["status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar='https://www.google.com/'):
        self.result["avatar"] = avatar

    def reset(self):
        self.set_avatar()
        self.set_balance()
        self.set_status()
        self.result["localize"]: {
                'en': Locale('en_US').build(),
                'ru': Locale('ru_RU').build()
        }
        return self

    def build(self):
        return self.result


x = Player().reset().build()
print(x)