import pytest
from client.credit_card import CreditCard


def test_card_json():
    card = CreditCard('123', 'visa')
    assert card == {}
