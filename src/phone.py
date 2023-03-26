from .item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __add__(self, other):
        if not isinstance(other, Phone):
            raise ValueError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


