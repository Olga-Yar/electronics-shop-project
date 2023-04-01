from src.item import Item


class MixinLog:
    __language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Функция для изменения языка
        """
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity, language='EN'):
        """
        Инициализация дочернего класса
        """
        super().__init__(name, price, quantity)
        self.__language = language



