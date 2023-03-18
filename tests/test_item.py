"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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



