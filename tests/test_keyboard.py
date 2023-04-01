import pytest
from src.keyboard import Keyboard


# @pytest.fixture
# def kb():
#     return Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == 'Dark Project KD87A'


def test_init():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'

