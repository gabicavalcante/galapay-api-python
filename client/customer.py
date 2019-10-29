from .utils.encoders import ObjectJsonSerializable


class Customer(ObjectJsonSerializable):
    """Class to represent the Customer.

    TODO:
    "Address": {
        "zipCode": "30411-325",
        "street": "Rua platina",
        "number": "1375",
        "neighborhood": "Prado",
        "city": "Belo Horizonte",
        "state": "MG",
        "complement": "2º andar"
    }
    """

    def __init__(self):
        self.document = None
        self.name = None
        self.email = None
        self.phone = None
        self.address = None
