from .utils.encoders import ObjectJsonSerializable


class GalaxPayClient(ObjectJsonSerializable):
    def __init__(self, sale, auth):
        self.sale = None
        self.auth = None

    def createPaymentBill(self):
        pass
