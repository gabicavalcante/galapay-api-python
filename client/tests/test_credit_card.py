import json
from client.credit_card import CreditCard

card_data = {
    "brand": "visa",
    "number": None,
    "cvv": "123",
    "expiryMonth": None,
    "expiryYear": None,
    "holder": None
}


def test_create_card_json():
    card = CreditCard('123', 'visa')
    assert isinstance(card, CreditCard)
    assert card.toJSON() == json.dumps(card_data,
                                       sort_keys=True, indent=4)
    assert card.cvv == card_data.get('cvv')
    assert card.brand == card_data.get('brand')


def test_get_brand():
    assert 'visa' == CreditCard.get_brand("4761 1200 0000 0148")
    assert 'mastercard' == CreditCard.get_brand("5168 4412 2363 0339")
    assert 'maestro' == CreditCard.get_brand("5080 7415 4958 8144 561")
    assert 'american express' == CreditCard.get_brand("3716 4219 0784 801")

    assert not CreditCard.get_brand('')
