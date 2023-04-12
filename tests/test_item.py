"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def product():
    return Item('Смартфон', 10, 2)


def test_total_price(product):
    """
    Проверка подсчета общей стоимости товара
    """
    assert product.calculate_total_price() == 20


def test_apply_discount_without(product):
    """
    Проверка стоимости товара с учетом скидки по умолчанию
    """
    product.apply_discount()
    assert product.price == 10


def test_name():
    """
    Проверка сеттера name
    """
    Item.name = 'СмартфонСмартфон'
    assert 'Длина наименования товара больше 10 символов'


def test_string_to_number():
    """
    Конвертирование строки-числа в число
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5


def test_instantiate_from_csv():
    item1 = Item.all
    assert item1 == ['Смартфон', '100', '1']


def test_instantiate_from_csv_filenotfound():
    with pytest.raises(FileNotFoundError):
        with open('nofile.csv', 'r') as f:
            content = f.read()


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError) as f:
        raise InstantiateCSVError('Файл item.csv поврежден')
    assert str(f.value) == 'Файл item.csv поврежден'


def test_repr():
    item1 = Item('Смартфон', 10, 2)
    assert repr(item1) == "Item('Смартфон', 10, 2)"


def test_str():
    item1 = Item('Смартфон', 10, 2)
    assert str(item1) == 'Смартфон'


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item('Смартфон', 10, 2)
    assert item1 + phone1 == 7