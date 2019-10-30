import json
from client.gclient import GalaxPayClient
from client.request import Request
from client.auth import Auth
from client.credit_card import CreditCard


payment_data = {
    "Auth": {
        "galaxId": "5473",
        "galaxHash": "83Mw5u8988Qj6fZqS4Z8K7LzOo1j28S706R0BeFe"
    },
    "Request": {
        "typeBill": "sale",
        "payday": "2018-06-21",
        "value": "80.00",
        "numberOfInstallments": "2",
        "paymentType": "newCard",
        "Card": {
            "number": "4716 0248 9944 1650",
            "holder": "Cliente de exemplo Galax Pay",
            "expiryMonth": "04",
            "expiryYear": "2023",
            "cvv": "541",
            "brand": "visa"
        }
    }
}


def test_create_card_json():

    card_payment = payment_data.get('Request').get('Card')
    card = CreditCard()
    card.cvv = '541'
    card.brand = 'visa'
    card.number = card_payment.get('number')
    card.holder = card_payment.get('holder')
    card.expiryMonth = card_payment.get('expiryMonth')
    card.expiryYear = card_payment.get('expiryYear')

    assert card.toJSON() == json.dumps(card_payment,
                                       sort_keys=True, indent=4)

    request_payment = payment_data.get('Request')
    request = Request(card=card)
    request.typeBill = request_payment.get('typeBill')
    request.payday = request_payment.get('payday')
    request.value = request_payment.get('value')
    request.numberOfInstallments = request_payment.get('numberOfInstallments')
    request.paymentType = request_payment.get('paymentType')

    assert request.toJSON() == json.dumps(request_payment,
                                          sort_keys=True, indent=4)

    auth = Auth()
    auth.read_config()

    assert auth.toJSON() == json.dumps(
        payment_data.get('Auth'), sort_keys=True, indent=4)

    client = GalaxPayClient(request, auth)

    assert isinstance(client, GalaxPayClient)
