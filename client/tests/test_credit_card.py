import pytest
import json
from client.credit_card import CreditCard

card_data = {
    "brand": "visa",
    "card_number": None,
    "cvv": "123",
    "expiryMonth": None,
    "expiryYear": None,
    "holder": None
}


def test_card_json():
    card = CreditCard('123', 'visa')
    assert isinstance(card, CreditCard)
    assert card.toJSON() == json.dumps(card_data,
                                       sort_keys=True, indent=4)
    assert card.cvv == card_data.get('cvv')
    assert card.brand == card_data.get('brand')
