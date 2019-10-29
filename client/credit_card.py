from .utils.encoders import ObjectJsonSerializable


class CreditCard(ObjectJsonSerializable):
    def __init__(self, cvv, brand):
        self.card_number = None
        self.holder = None
        self.expiryMonth = None
        self.expiryYear = None
        self.cvv = cvv
        self.brand = brand
