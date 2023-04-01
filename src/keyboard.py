from src.item import Item


class Keyboard(Item):

    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity)
        self.language = language

    def change_lang(self):
        if self.language == 'RU':
            self.language = 'EN'
        else:
            self.language = 'RU'

