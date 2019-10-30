from .utils.encoders import ObjectJsonSerializable


class Request(ObjectJsonSerializable):
    def __init__(self, customer=None, card=None):
        # self.Customer = customer
        self.Card = card

        self.quantity = None
        self.paymentType = None
        self.numberOfInstallments = None
        self.payday = None
        self.value = None
        self.typeBill = None
