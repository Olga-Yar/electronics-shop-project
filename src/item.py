import csv


class InstantiateCSVError(Exception):
    def __init__(self, ex):
        self.ex = ex


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            Exception('Длина наименования товара больше 10 символов')
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', 'r', encoding='windows-1251') as file:
            data = csv.reader(file)
            if file is None:
                raise FileNotFoundError('Отсутствует файл item.csv')
            else:
                for row in data:
                    if len(row) < 3:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        cls.all.append(row)
        return cls.all.pop(1)

    @staticmethod
    def string_to_number(data):
        data = int(float(data))
        return data

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.')
        return self.quantity + other.quantity